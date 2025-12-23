from groupdocs.parser import Parser

def calculate_container_size(file_path):
    """
    Calculate total size of all items in container.
    """
    with Parser(file_path) as parser:
        attachments = parser.get_container()
        
        if attachments is None:
            print("Container extraction not supported")
            return 0
        
        total_size = 0
        item_count = 0
        
        for attachment in attachments:
            total_size += attachment.size
            item_count += 1
        
        return {
            'total_size': total_size,
            'item_count': item_count,
            'average_size': total_size / item_count if item_count > 0 else 0
        }

# Usage
stats = calculate_container_size("archive.zip")

print(f"Container Statistics:")
print(f"  Items: {stats['item_count']}")
print(f"  Total Size: {stats['total_size']:,} bytes ({stats['total_size'] / 1024 / 1024:.2f} MB)")
print(f"  Average Size: {stats['average_size']:,.0f} bytes")