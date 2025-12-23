from groupdocs.parser import Parser

def process_archive_recursively(parser, level=0):
    """
    Recursively process archives and nested archives.
    """
    indent = "  " * level
    
    # Get container items
    attachments = parser.get_container()
    
    if not attachments:
        return
    
    for attachment in attachments:
        print(f"{indent} {attachment.name} ({attachment.size} bytes)")
        
        try:
            # Open parser for the attachment
            with attachment.open_parser() as file_parser:
                # Check if it's also a container (nested archive)
                nested_attachments = file_parser.get_container()
                
                if nested_attachments:
                    print(f"{indent}  └─ [Archive - processing nested items]")
                    process_archive_recursively(file_parser, level + 2)
                else:
                    # Try to extract text
                    text_reader = file_parser.get_text()
                    if text_reader:
                        text = text_reader
                        print(f"{indent}  └─ Text: {len(text)} characters")
        
        except Exception as e:
            print(f"{indent}  └─ Error: {e}")

# Usage
print("Archive Structure:\n")
with Parser("nested_archive.zip") as parser:
    process_archive_recursively(parser)