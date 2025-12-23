from groupdocs.parser import Parser
import os

def filter_by_extension(file_path, extensions):
    """
    Filter container items by file extension.
    
    Args:
        file_path: Path to container
        extensions: List of extensions to include (e.g., ['.pdf', '.docx'])
    """
    with Parser(file_path) as parser:
        attachments = parser.get_container()
        
        if attachments is None:
            print("Container extraction not supported")
            return []
        
        filtered_items = []
        
        for attachment in attachments:
            file_ext = os.path.splitext(attachment.name)[1].lower()
            
            if file_ext in extensions:
                filtered_items.append({
                    'name': attachment.name,
                    'size': attachment.size,
                    'extension': file_ext
                })
        
        return filtered_items

# Usage - find all PDF and Word documents
items = filter_by_extension("archive.zip", ['.pdf', '.docx', '.doc'])

print(f"Found {len(items)} PDF/Word documents:
")
for item in items:
    print(f"  {item['name']} ({item['size']:,} bytes)")