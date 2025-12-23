from groupdocs.parser import Parser

def get_metadata_value(metadata, field_name):
    """
    Get a specific metadata value by field name.
    """
    for item in metadata:
        if item.name.lower() == field_name.lower():
            return item.value
    return None

# Create an instance of Parser class
with Parser("document.docx") as parser:
    # Extract metadata
    metadata = parser.get_metadata()
    
    if metadata:
        # Convert to list for reuse
        metadata_list = list(metadata)
        
        # Extract specific fields
        author = get_metadata_value(metadata_list, "Author")
        title = get_metadata_value(metadata_list, "Title")
        created = get_metadata_value(metadata_list, "CreatedTime")
        modified = get_metadata_value(metadata_list, "ModifiedTime")
        
        # Print specific metadata
        print(f"Document Information:")
        print(f"  Title: {title}")
        print(f"  Author: {author}")
        print(f"  Created: {created}")
        print(f"  Modified: {modified}")