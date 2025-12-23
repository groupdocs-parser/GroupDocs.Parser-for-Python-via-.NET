from groupdocs.parser import Parser

# Create an instance of Parser class
with Parser("./sample.pdf") as parser:
    # Extract metadata from the document
    metadata = parser.get_metadata()
    
    # Check if metadata extraction is supported
    if metadata is None:
        print("Metadata extraction isn't supported")
    else:
        # Iterate over metadata items
        for item in metadata:
            # Print metadata name and value
            print(f"{item.name}: {item.value}")