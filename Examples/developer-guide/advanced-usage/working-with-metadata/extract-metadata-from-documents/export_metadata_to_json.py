from groupdocs.parser import Parser
import json

def export_metadata_to_json(file_path, output_file):
    """
    Extract metadata and save to JSON file.
    """
    with Parser(file_path) as parser:
        metadata = parser.get_metadata()
        
        if metadata is None:
            print("Metadata extraction not supported")
            return False
        
        # Build metadata dictionary
        metadata_dict = {
            'file_path': file_path,
            'properties': {}
        }
        
        for item in metadata:
            # Convert value to string for JSON serialization
            value = str(item.value) if item.value is not None else None
            metadata_dict['properties'][item.name] = value
        
        # Save to JSON
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(metadata_dict, f, indent=2, ensure_ascii=False)
        
        print(f"Metadata exported to {output_file}")
        return True

# Usage
export_metadata_to_json("sample.docx", "metadata.json")