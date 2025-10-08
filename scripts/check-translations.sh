#!/bin/bash
# Script to check translation progress
# Скрипт для перевірки прогресу перекладу
# Скрипт для проверки прогресса перевода

set -e

DOCS_DIR="docs"
LOCALE_DIR="$DOCS_DIR/locale"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo "╔════════════════════════════════════════════════╗"
echo "║  Translation Progress Check                    ║"
echo "║  Перевірка прогресу перекладу                  ║"
echo "║  Проверка прогресса перевода                   ║"
echo "╚════════════════════════════════════════════════╝"
echo ""

# Check if msgfmt is installed
if ! command -v msgfmt &> /dev/null; then
    echo "❌ msgfmt not found. Please install gettext:"
    echo "   sudo apt-get install gettext"
    exit 1
fi

# Function to check language
check_language() {
    local lang=$1
    local lang_name=$2
    
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}Language: $lang_name ($lang)${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    
    if [ ! -d "$LOCALE_DIR/$lang" ]; then
        echo "❌ No translations found for $lang"
        return
    fi
    
    total_translated=0
    total_fuzzy=0
    total_untranslated=0
    
    for po_file in "$LOCALE_DIR/$lang/LC_MESSAGES"/*.po; do
        if [ -f "$po_file" ]; then
            filename=$(basename "$po_file")
            echo ""
            echo "📄 $filename:"
            
            # Get statistics
            stats=$(msgfmt --statistics "$po_file" 2>&1)
            echo "   $stats"
            
            # Extract numbers (rough parsing)
            translated=$(echo "$stats" | grep -oP '\d+(?= translated)' || echo "0")
            fuzzy=$(echo "$stats" | grep -oP '\d+(?= fuzzy)' || echo "0")
            untranslated=$(echo "$stats" | grep -oP '\d+(?= untranslated)' || echo "0")
            
            total_translated=$((total_translated + translated))
            total_fuzzy=$((total_fuzzy + fuzzy))
            total_untranslated=$((total_untranslated + untranslated))
        fi
    done
    
    echo ""
    echo "📊 Total for $lang_name:"
    echo "   ✅ Translated: $total_translated"
    if [ $total_fuzzy -gt 0 ]; then
        echo -e "   ${YELLOW}⚠️  Fuzzy: $total_fuzzy${NC}"
    fi
    if [ $total_untranslated -gt 0 ]; then
        echo -e "   ${YELLOW}❌ Untranslated: $total_untranslated${NC}"
    fi
    
    total_messages=$((total_translated + total_fuzzy + total_untranslated))
    if [ $total_messages -gt 0 ]; then
        percentage=$((total_translated * 100 / total_messages))
        echo "   📈 Progress: $percentage%"
    fi
    echo ""
}

# Check all languages
check_language "uk" "Ukrainian / Українська"
check_language "ru" "Russian / Русский"

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "💡 To update translations:"
echo "   make gettext     # Extract messages"
echo "   make update      # Update .po files"
echo "   make html-all    # Build all languages"
echo ""
echo "📖 See LOCALIZATION.md for detailed guide"
echo ""

