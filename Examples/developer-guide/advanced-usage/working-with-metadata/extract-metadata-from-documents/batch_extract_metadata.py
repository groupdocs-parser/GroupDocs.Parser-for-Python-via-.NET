from groupdocs.parser import Parser
from pathlib import Path
import csv

def batch_extract_metadata(input_dir, output_csv):
    """
    Extract metadata from all documents in a directory and save to CSV.
    """
    extensions = ['.pdf', '.docx', '.doc', '.xlsx', '.xls', '.pptx', '.ppt']
    
    results = []
    
    for file_path in Path(input_dir).rglob('*'):
        if file_path.suffix.lower() in extensions:
            print(f"Processing: {file_path.name}")
            
            try:
                with Parser(str(file_path)) as parser:
                    metadata = parser.get_metadata()
                    
                    if metadata:
                        # Extract common fields
                        meta_dict = {'file_name': file_path.name}
                        
                        for item in metadata:
                            meta_dict[item.name] = str(item.value) if item.value else ""
                        
                        results.append(meta_dict)
                    
            except Exception as e:
                print(f"  Error: {e}")
    
    # Save to CSV
    if results:
        # Get all unique field names
        all_fields = set()
        for result in results:
            all_fields.update(result.keys())
        
        # Write CSV
        with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=sorted(all_fields))
            writer.writeheader()
            writer.writerows(results)
        
        print(f"
Extracted metadata from {len(results)} documents")
        print(f"Saved to {output_csv}")

# Usage
batch_extract_metadata("documents", "metadata_report.csv")