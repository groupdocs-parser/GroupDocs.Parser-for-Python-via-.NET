from groupdocs.parser import Parser

def get_supported_items(file_path):
    """
    Get list of items that support text extraction.
    """
    with Parser(file_path) as parser:
        attachments = parser.get_container()
        
        if attachments is None:
            print("Container extraction not supported")
            return []
        
        supported = []
        unsupported = []
        
        for attachment in attachments:
            try:
                with attachment.open_parser() as file_parser:
                    # Check if text extraction is supported
                    if file_parser.features.text:
                        info = file_parser.get_document_info()
                        file_type = info.file_type.file_format if info and info.file_type else "Unknown"
                        
                        supported.append({
                            'name': attachment.name,
                            'type': file_type,
                            'size': attachment.size
                        })
                    else:
                        unsupported.append(attachment.name)
            
            except:
                unsupported.append(attachment.name)
        
        return {
            'supported': supported,
            'unsupported': unsupported
        }

# Usage
result = get_supported_items("documents.zip")

print(f"Supported files ({len(result['supported'])}):")
for item in result['supported']:
    print(f"  {item['name']} [{item['type']}]")

print(f"
Unsupported files ({len(result['unsupported'])}):")
for name in result['unsupported']:
    print(f"  {name}")