"""Sphinx extension: rewrite relative links in shared submodule includes."""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Callable

import docutils.parsers.rst.directives.misc as _rst_misc
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


def _rewrite_fn_for_path(path: Path, default_branch: str) -> Callable[[str], str] | None:
    parts = _submodule_file_parts(path)
    if parts is None:
        return None

    submodule_name, file_rel = parts
    submodules = discover_submodules(_REPO_ROOT, default_branch=default_branch)
    info = submodules.get(submodule_name)
    if info is None:
        return None

    return lambda text: rewrite_content(text, info, file_rel)


@contextmanager
def _patch_fileinput(resolved: Path, rewrite_fn: Callable[[str], str]):
    """Rewrite ``FileInput.read()`` for a single shared submodule include."""
    original = _rst_misc.io.FileInput

    class RewritingFileInput(original):
        def read(self):
            data = super().read()
            if self.source_path and Path(self.source_path).resolve() == resolved:
                return rewrite_fn(data)
            return data

    _rst_misc.io.FileInput = RewritingFileInput
    try:
        yield
    finally:
        _rst_misc.io.FileInput = original


def _on_include_read(app, path, docname, arg) -> None:
    """Rewrite relative links for includes that emit ``include-read``."""
    resolved = (Path(app.srcdir) / Path(path)).resolve()
    rewrite_fn = _rewrite_fn_for_path(
        resolved, app.config.shared_include_default_branch
    )
    if rewrite_fn is None:
        return
    arg[0] = rewrite_fn(arg[0])


class SharedRewritingInclude(SphinxInclude):
    """Standard ``include`` with link rewriting for files under ``shared/``."""

    def run(self):
        if self.arguments[0].startswith('<') and self.arguments[0].endswith('>'):
            return super().run()

        _rel_filename, filename = self.env.relfn2path(self.arguments[0])
        self.arguments[0] = str(filename)
        self.env.note_included(filename)

        resolved = Path(filename).resolve()
        rewrite_fn = _rewrite_fn_for_path(
            resolved, self.env.config.shared_include_default_branch
        )
        if rewrite_fn is None:
            return super().run()

        with _patch_fileinput(resolved, rewrite_fn):
            return super().run()


def setup(app):
    app.add_config_value('shared_include_default_branch', 'main', 'env')
    app.connect('include-read', _on_include_read)
    app.add_directive('include', SharedRewritingInclude, override=True)

    return {
        'version': '1.3.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
