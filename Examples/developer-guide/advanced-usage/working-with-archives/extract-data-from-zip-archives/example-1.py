from groupdocs.parser import Parser

# Create an instance of Parser class
with Parser("./archive.zip") as parser:
    # Get container items (files in the archive)
    attachments = parser.get_container()
    
    # Check if container extraction is supported
    if attachments is None:
        print("Container extraction isn't supported")
    else:
        # Iterate over attachments
        for idx, attachment in enumerate(attachments):
            print(f"
File {idx + 1}:")
            print(f"  Name: {attachment.name}")
            print(f"  Size: {attachment.size} bytes")
            print(f"  File Path: {attachment.file_path}")