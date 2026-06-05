"""Sphinx extension: rewrite relative links in shared submodule includes."""

from __future__ import annotations

from pathlib import Path

from sphinx.directives.other import Include as SphinxInclude

from .discovery import discover_submodules
from .rewrite import rewrite_content

_REPO_ROOT = Path(__file__).resolve().parents[3]
_SHARED_ROOT = _REPO_ROOT / 'shared'


def _is_under_shared(path: Path) -> bool:
    try:
        path.resolve().relative_to(_SHARED_ROOT.resolve())
        return True
    except ValueError:
        return False


def _submodule_file_parts(path: Path) -> tuple[str, str] | None:
    """Return ``(submodule_name, file_rel)`` for a path under ``shared/``."""
    try:
        rel = path.resolve().relative_to(_SHARED_ROOT.resolve())
    except ValueError:
        return None
    if len(rel.parts) < 2:
        return None
    return rel.parts[0], '/'.join(rel.parts[1:])


class SharedRewritingInclude(SphinxInclude):
    """Standard ``include`` with link rewriting for files under ``shared/``."""

    def read_file(self, path) -> str:
        text = super().read_file(path)
        resolved = Path(path).resolve()
        if not _is_under_shared(resolved):
            return text

        parts = _submodule_file_parts(resolved)
        if parts is None:
            return text

        submodule_name, file_rel = parts
        default_branch = self.env.config.shared_include_default_branch
        submodules = discover_submodules(_REPO_ROOT, default_branch=default_branch)
        info = submodules.get(submodule_name)
        if info is None:
            return text

        return rewrite_content(text, info, file_rel)


def setup(app):
    app.add_config_value('shared_include_default_branch', 'main', 'env')
    app.add_directive('include', SharedRewritingInclude, override=True)

    return {
        'version': '1.2.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
