from groupdocs.parser import Parser

with Parser("sample.pptx") as parser:
    # Use format-specific text extraction methods exposed in the API reference
    reader = parser.get_text()
    print(reader if reader else "Formatted text isn't available.")