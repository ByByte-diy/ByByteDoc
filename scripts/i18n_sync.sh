#!/usr/bin/env bash
set -euo pipefail

# i18n end-to-end helper for Sphinx
# Usage:
#   scripts/i18n_sync.sh gettext         # regenerate POT catalogs
#   scripts/i18n_sync.sh update          # update PO for uk/ru
#   scripts/i18n_sync.sh import          # import RST uk/ru into PO (nano index/spec)
#   scripts/i18n_sync.sh fixpo           # collapse multiline msgstr in PO
#   scripts/i18n_sync.sh clean-suffix    # remove *.uk.po *.ru.po
#   scripts/i18n_sync.sh build [lang]    # build for a language (uk|ru|en)

ROOT=$(cd "$(dirname "$0")/.." && pwd)
DOCS="$ROOT/docs"

case "${1:-}" in
  gettext)
    make -C "$ROOT" gettext
    ;;
  update)
    make -C "$ROOT" update
    ;;
  import)
    python3 "$ROOT/scripts/import_translations.py"
    ;;
  fixpo)
    python3 "$ROOT/scripts/fix_po_msgstr.py"
    ;;
  clean-suffix)
    find "$DOCS/locale" -type f \( -name "*.uk.po" -o -name "*.ru.po" \) -delete || true
    ;;
  build)
    lang=${2:-uk}
    make -C "$ROOT" html-${lang}
    ;;
  stats)
    python3 "$ROOT/scripts/update_translation_stats.py"
    ;;
  *)
    echo "Usage: $0 {gettext|update|import|fixpo|clean-suffix|build [uk|ru|en]|stats}" >&2
    exit 1
    ;;
esac


