from groupdocs.parser import Parser
import re

def search_container_items(file_path, pattern):
    """
    Search for items matching a name pattern.
    
    Args:
        file_path: Path to container
        pattern: Regex pattern to match file names
    """
    with Parser(file_path) as parser:
        attachments = parser.get_container()
        
        if attachments is None:
            print("Container extraction not supported")
            return []
        
        regex = re.compile(pattern, re.IGNORECASE)
        matches = []
        
        for attachment in attachments:
            if regex.search(attachment.name):
                matches.append({
                    'name': attachment.name,
                    'size': attachment.size,
                    'path': attachment.file_path
                })
        
        return matches

# Usage - find all files containing "invoice"
matches = search_container_items("documents.zip", r'invoice')

print(f"Found {len(matches)} matching files:
")
for match in matches:
    print(f"  {match['name']} ({match['size']:,} bytes)")