from groupdocs.parser import Parser
import json

def create_archive_inventory(archive_path, output_json):
    """
    Create detailed inventory of ZIP archive contents.
    """
    inventory = {
        'archive': archive_path,
        'total_files': 0,
        'total_size': 0,
        'files': []
    }
    
    with Parser(archive_path) as parser:
        attachments = parser.get_container()
        
        if attachments:
            for attachment in attachments:
                file_entry = {
                    'name': attachment.name,
                    'size': attachment.size,
                    'path': attachment.file_path,
                    'extractable': False
                }
                
                try:
                    with attachment.open_parser() as file_parser:
                        # Check if text extraction is supported
                        if file_parser.features.text:
                            text_reader = file_parser.get_text()
                            if text_reader:
                                text = text_reader
                                file_entry['extractable'] = True
                                file_entry['text_length'] = len(text)
                                file_entry['word_count'] = len(text.split())
                except:
                    pass
                
                inventory['files'].append(file_entry)
                inventory['total_size'] += attachment.size
                inventory['total_files'] += 1
    
    # Save to JSON
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(inventory, f, indent=2, ensure_ascii=False)
    
    print(f"Inventory created: {output_json}")
    print(f"  Total files: {inventory['total_files']}")
    print(f"  Total size: {inventory['total_size']:,} bytes")
    print(f"  Extractable: {sum(1 for f in inventory['files'] if f['extractable'])}")

# Usage
create_archive_inventory("archive.zip", "inventory.json")