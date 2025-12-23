from groupdocs.parser import Parser

# Create an instance of Parser class
with Parser("./archive.zip") as parser:
    # Get container items
    attachments = parser.get_container()
    
    # Check if container extraction is supported
    if attachments is None:
        print("Container extraction isn't supported")
    else:
        # Iterate over items
        for idx, attachment in enumerate(attachments):
            print(f"
Item {idx + 1}:")
            print(f"  Name: {attachment.name}")
            print(f"  Size: {attachment.size} bytes")
            print(f"  Path: {attachment.file_path}")