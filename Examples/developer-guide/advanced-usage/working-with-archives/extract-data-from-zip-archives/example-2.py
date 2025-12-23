from groupdocs.parser import Parser

# Create an instance of Parser class for the archive
with Parser("./documents.zip") as parser:
    # Get container items
    attachments = parser.get_container()
    
    if attachments is None:
        print("Container extraction not supported")
    else:
        # Iterate over attachments
        for attachment in attachments:
            print(f"
Processing: {attachment.name}")
            
            try:
                # Get parser for the attachment
                with attachment.open_parser() as file_parser:
                    # Extract text from the file
                    text_reader = file_parser.get_text()
                    
                    if text_reader:
                        text = text_reader
                        print(f"  Extracted {len(text)} characters")
                        print(f"  Preview: {text[:100]}...")
                    else:
                        print(f"  Text extraction not supported for this file")
            
            except Exception as e:
                print(f"  Error: {e}")