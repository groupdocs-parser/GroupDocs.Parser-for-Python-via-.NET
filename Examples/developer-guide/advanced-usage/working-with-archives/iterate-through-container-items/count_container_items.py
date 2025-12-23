from groupdocs.parser import Parser

def count_container_items(file_path):
    """
    Count the number of items in a container.
    """
    with Parser(file_path) as parser:
        attachments = parser.get_container()
        
        if attachments is None:
            return 0
        
        # Convert to list to count
        items = list(attachments)
        return len(items)

# Usage
count = count_container_items("archive.zip")
print(f"Container has {count} items")