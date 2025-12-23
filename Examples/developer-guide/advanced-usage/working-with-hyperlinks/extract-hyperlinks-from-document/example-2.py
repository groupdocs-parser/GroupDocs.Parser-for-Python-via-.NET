from groupdocs.parser import Parser

# Create an instance of Parser class
with Parser("document.docx") as parser:
    # Check if hyperlink extraction is supported
    if not parser.features.hyperlinks:
        print("Hyperlink extraction not supported")
        return
    
    # Extract hyperlinks
    hyperlinks = parser.get_hyperlinks()
    
    if hyperlinks:
        for idx, hyperlink in enumerate(hyperlinks):
            print(f"Hyperlink {idx + 1}:")
            print(f"  Text: {hyperlink.text}")
            print(f"  URL: {hyperlink.url}")
            print(f"  Page: {hyperlink.page.index + 1}")
            print(f"  Position: ({hyperlink.rectangle.left}, {hyperlink.rectangle.top})")
            print(f"  Size: {hyperlink.rectangle.width}x{hyperlink.rectangle.height}")
            print()