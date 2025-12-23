from groupdocs.parser import Parser

# Create an instance of Parser class
with Parser("./sample.pdf") as parser:
    # Check if hyperlink extraction is supported
    if not parser.features.hyperlinks:
        print("Document doesn't support hyperlink extraction")
        return
    
    # Extract hyperlinks from the document
    hyperlinks = parser.get_hyperlinks()
    
    if hyperlinks:
        # Iterate over hyperlinks
        for hyperlink in hyperlinks:
            # Print the hyperlink text
            print(f"Text: {hyperlink.text}")
            # Print the hyperlink URL
            print(f"URL: {hyperlink.url}")
            # Print page number
            print(f"Page: {hyperlink.page.index + 1}")
            print()