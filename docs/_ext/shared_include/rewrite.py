"""Rewrite relative links in submodule Markdown to absolute GitHub URLs."""

from __future__ import annotations

import os
import re
from pathlib import Path

from .discovery import SubmoduleInfo

_ABSOLUTE_RE = re.compile(r'^(https?:|mailto:|tel:|ftp:|#|//)')
_MD_LINK_RE = re.compile(r'(!?\[[^\]]*\])\(\s*(<[^>]+>|[^)\s]+)([^)]*)\)')
_HTML_ATTR_RE = re.compile(r'''(?P<attr>src|href)\s*=\s*["'](?P<url>[^"']+)["']''', re.I)

_IMAGE_EXTENSIONS = frozenset({'.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg', '.ico'})


def _is_image(path: str, *, html_attr: str | None = None) -> bool:
    if html_attr == 'src':
        return True
    return Path(path.split('#')[0]).suffix.lower() in _IMAGE_EXTENSIONS


def _resolve_target(
    target: str,
    file_dir: str,
    info: SubmoduleInfo,
    *,
    force_raw: bool = False,
) -> str:
    target = target.strip('<>')
    if _ABSOLUTE_RE.match(target):
        return target

    url, sep, anchor = target.partition('#')
    if not url:
        return target

    if file_dir:
        resolved = os.path.normpath(os.path.join(file_dir, url)).replace('\\', '/')
    else:
        resolved = url.lstrip('./')

    base = info.raw_base if (force_raw or _is_image(url)) else info.blob_base
    new_url = f'{base}/{resolved}'
    if sep:
        new_url = f'{new_url}#{anchor}'
    return new_url


def rewrite_content(text: str, info: SubmoduleInfo, file_rel: str) -> str:
    """Rewrite relative Markdown and HTML links in *text*."""
    file_dir = Path(file_rel).parent.as_posix()
    if file_dir == '.':
        file_dir = ''

    def md_repl(match: re.Match[str]) -> str:
        label, target, trailer = match.group(1), match.group(2), match.group(3)
        new_target = _resolve_target(target, file_dir, info)
        return f'{label}({new_target}{trailer})'

    def html_repl(match: re.Match[str]) -> str:
        attr = match.group('attr').lower()
        url = match.group('url')
        new_url = _resolve_target(url, file_dir, info, force_raw=(attr == 'src'))
        return f'{attr}="{new_url}"'

    text = _MD_LINK_RE.sub(md_repl, text)
    text = _HTML_ATTR_RE.sub(html_repl, text)
    return text
