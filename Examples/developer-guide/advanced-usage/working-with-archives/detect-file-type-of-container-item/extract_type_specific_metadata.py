from groupdocs.parser import Parser

def extract_type_specific_metadata(file_path):
    """
    Extract metadata specific to each file type.
    """
    with Parser(file_path) as parser:
        attachments = parser.get_container()
        
        if attachments is None:
            print("Container extraction not supported")
            return
        
        for attachment in attachments:
            print(f"
{'='*60}")
            print(f"File: {attachment.name}")
            
            try:
                with attachment.open_parser() as file_parser:
                    info = file_parser.get_document_info()
                    
                    if info and info.file_type:
                        print(f"Type: {info.file_type.file_format}")
                        
                        # Get metadata
                        metadata = file_parser.get_metadata()
                        
                        if metadata:
                            print("\nMetadata:")
                            for item in metadata:
                                print(f"  {item.name}: {item.value}")
                        
                        # Get page count if available
                        if hasattr(info, 'page_count'):
                            print(f"\nPages: {info.page_count}")
            
            except Exception as e:
                print(f"Error: {e}")

# Usage
extract_type_specific_metadata("mixed_documents.zip")