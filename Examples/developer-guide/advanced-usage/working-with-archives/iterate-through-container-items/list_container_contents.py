from groupdocs.parser import Parser

def list_container_contents(file_path):
    """
    List all container contents with detailed information.
    """
    with Parser(file_path) as parser:
        attachments = parser.get_container()
        
        if attachments is None:
            print("Container extraction not supported")
            return
        
        print(f"{'#':<5}{'Name':<40}{'Size':<15}{'Path':<30}")
        print("-" * 90)
        
        for idx, attachment in enumerate(attachments, 1):
            name = attachment.name[:38] if len(attachment.name) > 38 else attachment.name
            size = f"{attachment.size:,} bytes"
            path = attachment.file_path[:28] if attachment.file_path and len(attachment.file_path) > 28 else (attachment.file_path or "")
            
            print(f"{idx:<5}{name:<40}{size:<15}{path:<30}")

# Usage
list_container_contents("documents.zip")