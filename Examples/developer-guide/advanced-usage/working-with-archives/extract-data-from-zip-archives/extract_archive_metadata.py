from groupdocs.parser import Parser

def extract_archive_metadata(archive_path):
    """
    Extract metadata from all files in an archive.
    """
    results = []
    
    with Parser(archive_path) as parser:
        attachments = parser.get_container()
        
        if not attachments:
            print("No files in archive")
            return results
        
        for attachment in attachments:
            file_info = {
                'name': attachment.name,
                'size': attachment.size,
                'path': attachment.file_path
            }
            
            try:
                with attachment.open_parser() as file_parser:
                    # Get metadata
                    metadata = file_parser.get_metadata()
                    
                    if metadata:
                        file_info['metadata'] = {}
                        for item in metadata:
                            file_info['metadata'][item.name] = str(item.value)
                    
                    # Get document info
                    info = file_parser.get_document_info()
                    if info:
                        file_info['file_type'] = info.file_type.extension
                        file_info['page_count'] = info.page_count
            
            except Exception as e:
                file_info['error'] = str(e)
            
            results.append(file_info)
    
    return results

# Usage
metadata_list = extract_archive_metadata("documents.zip")

print("Archive Metadata Report:\n")
for item in metadata_list:
    print(f"File: {item['name']}")
    print(f"  Size: {item['size']} bytes")
    if 'file_type' in item:
        print(f"  Type: {item['file_type']}")
    if 'page_count' in item:
        print(f"  Pages: {item['page_count']}")
    if 'metadata' in item:
        print(f"  Metadata: {len(item['metadata'])} properties")
    print()