from groupdocs.parser import Parser

# Create an instance of Parser class
with Parser("./document.pdf") as parser:
    # Check if hyperlink extraction is supported
    if not parser.features.hyperlinks:
        print("Hyperlink extraction not supported")
        return
    
    # Extract hyperlinks from page 0 (first page)
    page_index = 0
    hyperlinks = parser.get_hyperlinks(page_index)
    
    if hyperlinks:
        print(f"Hyperlinks on page {page_index + 1}:")
        for link in hyperlinks:
            print(f"  Text: {link.text}")
            print(f"  URL: {link.url}")
            print()