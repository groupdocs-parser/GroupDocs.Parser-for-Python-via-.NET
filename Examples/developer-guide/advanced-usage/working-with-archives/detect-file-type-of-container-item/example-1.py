from groupdocs.parser import Parser

# Create an instance of Parser class
with Parser("./archive.zip") as parser:
    # Get container items
    attachments = parser.get_container()
    
    if attachments is None:
        print("Container extraction not supported")
    else:
        # Iterate over attachments
        for attachment in attachments:
            print(f"
File: {attachment.name}")
            
            try:
                # Open parser for the attachment
                with attachment.open_parser() as file_parser:
                    # Get document info to detect file type
                    info = file_parser.get_document_info()
                    
                    if info and info.file_type:
                        print(f"  Type: {info.file_type.file_format}")
                        print(f"  Extension: {info.file_type.extension}")
                    else:
                        print(f"  Type: Unknown")
            
            except Exception as e:
                print(f"  Error: {e}")