from groupdocs.parser import Parser
from collections import defaultdict
import os

def group_by_file_type(file_path):
    """
    Group container items by file extension.
    """
    with Parser(file_path) as parser:
        attachments = parser.get_container()
        
        if attachments is None:
            print("Container extraction not supported")
            return {}
        
        groups = defaultdict(list)
        
        for attachment in attachments:
            ext = os.path.splitext(attachment.name)[1].lower() or 'no_extension'
            groups[ext].append({
                'name': attachment.name,
                'size': attachment.size
            })
        
        return dict(groups)

# Usage
groups = group_by_file_type("mixed_archive.zip")

print("Files grouped by type:\n")
for ext, items in sorted(groups.items()):
    total_size = sum(item['size'] for item in items)
    print(f"{ext.upper()} files: {len(items)} items, {total_size:,} bytes")
    for item in items[:3]:  # Show first 3
        print(f"  - {item['name']}")
    if len(items) > 3:
        print(f"  ... and {len(items) - 3} more")
    print()