from groupdocs.parser import Parser
from collections import defaultdict

def categorize_by_file_type(file_path):
    """
    Categorize container items by detected file type.
    """
    with Parser(file_path) as parser:
        attachments = parser.get_container()
        
        if attachments is None:
            print("Container extraction not supported")
            return {}
        
        categories = defaultdict(list)
        
        for attachment in attachments:
            try:
                with attachment.open_parser() as file_parser:
                    info = file_parser.get_document_info()
                    
                    if info and info.file_type:
                        file_type = info.file_type.file_format
                    else:
                        file_type = "Unknown"
            
            except:
                file_type = "Error"
            
            categories[file_type].append(attachment.name)
        
        return dict(categories)

# Usage
categories = categorize_by_file_type("mixed_files.zip")

print("Files categorized by type:\n")
for file_type, files in sorted(categories.items()):
    print(f"{file_type}: {len(files)} files")
    for filename in files[:3]:  # Show first 3
        print(f"  - {filename}")
    if len(files) > 3:
        print(f"  ... and {len(files) - 3} more")
    print()