"""Discover git submodules and resolve GitHub remote URLs."""

from __future__ import annotations

import configparser
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class SubmoduleInfo:
    """Metadata for a git submodule under ``shared/``."""

    name: str
    path: Path
    owner: str
    repo: str
    branch: str

    @property
    def blob_base(self) -> str:
        return f'https://github.com/{self.owner}/{self.repo}/blob/{self.branch}'

    @property
    def raw_base(self) -> str:
        return f'https://raw.githubusercontent.com/{self.owner}/{self.repo}/{self.branch}'


_GITHUB_REMOTE_RE = re.compile(
    r'github\.com[:/](?P<owner>[^/]+)/(?P<repo>[^/]+?)(?:\.git)?/?$'
)


def parse_github_remote(url: str) -> tuple[str, str] | None:
    """Return ``(owner, repo)`` from a GitHub remote URL, or ``None``."""
    match = _GITHUB_REMOTE_RE.search(url.strip())
    if not match:
        return None
    return match.group('owner'), match.group('repo')


def get_branch(submodule_path: Path, default: str = 'main') -> str:
    """Return the checked-out branch of a submodule, or *default* if detached."""
    try:
        result = subprocess.run(
            ['git', '-C', str(submodule_path), 'rev-parse', '--abbrev-ref', 'HEAD'],
            capture_output=True,
            text=True,
            check=True,
        )
        branch = result.stdout.strip()
        if branch and branch != 'HEAD':
            return branch
    except (OSError, subprocess.CalledProcessError):
        pass
    return default


def get_remote_url(submodule_path: Path) -> str | None:
    """Return ``remote.origin.url`` for a submodule checkout."""
    try:
        result = subprocess.run(
            ['git', '-C', str(submodule_path), 'config', '--get', 'remote.origin.url'],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip() or None
    except (OSError, subprocess.CalledProcessError):
        return None


def discover_submodules(
    repo_root: Path,
    *,
    default_branch: str = 'main',
) -> dict[str, SubmoduleInfo]:
    """Build a name → info map from ``.gitmodules`` and live git remotes."""
    gitmodules = repo_root / '.gitmodules'
    if not gitmodules.is_file():
        return {}

    config = configparser.ConfigParser()
    config.read(gitmodules, encoding='utf-8')

    submodules: dict[str, SubmoduleInfo] = {}
    for section in config.sections():
        if not section.startswith('submodule '):
            continue
        rel_path = config.get(section, 'path', fallback='').strip()
        if not rel_path:
            continue

        submodule_path = (repo_root / rel_path).resolve()
        name = Path(rel_path).name

        remote = get_remote_url(submodule_path)
        if not remote:
            continue
        parsed = parse_github_remote(remote)
        if not parsed:
            continue

        owner, repo = parsed
        branch = get_branch(submodule_path, default_branch)
        submodules[name] = SubmoduleInfo(
            name=name,
            path=submodule_path,
            owner=owner,
            repo=repo,
            branch=branch,
        )

    return submodules
