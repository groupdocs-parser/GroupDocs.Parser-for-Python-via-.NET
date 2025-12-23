from groupdocs.parser import Parser

def validate_container_contents(file_path, expected_types):
    """
    Validate that container only contains expected file types.
    
    Args:
        file_path: Path to container
        expected_types: List of expected file formats (e.g., ['Pdf', 'Docx'])
    """
    with Parser(file_path) as parser:
        attachments = parser.get_container()
        
        if attachments is None:
            print("Container extraction not supported")
            return False
        
        valid_items = []
        invalid_items = []
        
        for attachment in attachments:
            try:
                with attachment.open_parser() as file_parser:
                    info = file_parser.get_document_info()
                    
                    if info and info.file_type:
                        file_type = info.file_type.file_format
                        
                        if file_type in expected_types:
                            valid_items.append({
                                'name': attachment.name,
                                'type': file_type
                            })
                        else:
                            invalid_items.append({
                                'name': attachment.name,
                                'type': file_type,
                                'reason': 'Unexpected type'
                            })
                    else:
                        invalid_items.append({
                            'name': attachment.name,
                            'type': 'Unknown',
                            'reason': 'Type not detected'
                        })
            
            except Exception as e:
                invalid_items.append({
                    'name': attachment.name,
                    'type': 'Error',
                    'reason': str(e)
                })
        
        # Print results
        print(f"Validation Results:")
        print(f"  Valid items: {len(valid_items)}")
        print(f"  Invalid items: {len(invalid_items)}
")
        
        if invalid_items:
            print("Invalid items:")
            for item in invalid_items:
                print(f"  {item['name']}: {item['type']} - {item['reason']}")
        
        return len(invalid_items) == 0

# Usage - validate that archive contains only PDFs and Word documents
is_valid = validate_container_contents("documents.zip", ['Pdf', 'Docx', 'Doc'])
print(f"
Container is valid: {is_valid}")