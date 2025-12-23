from groupdocs.parser import Parser
from pathlib import Path
import json

def batch_extract_hyperlinks(input_dir, output_json):
    """
    Extract hyperlinks from all documents in a directory.
    """
    extensions = ['.pdf', '.docx', '.doc', '.html', '.htm']
    
    all_hyperlinks = {}
    
    for file_path in Path(input_dir).rglob('*'):
        if file_path.suffix.lower() in extensions:
            print(f"Processing: {file_path.name}")
            
            try:
                with Parser(str(file_path)) as parser:
                    if not parser.features.hyperlinks:
                        continue
                    
                    hyperlinks = parser.get_hyperlinks()
                    
                    if hyperlinks:
                        link_list = []
                        for link in hyperlinks:
                            link_list.append({
                                'text': link.text or '',
                                'url': link.url or '',
                                'page': link.page.index + 1
                            })
                        
                        all_hyperlinks[file_path.name] = {
                            'count': len(link_list),
                            'links': link_list
                        }
                
            except Exception as e:
                print(f"  Error: {e}")
    
    # Save to JSON
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(all_hyperlinks, f, indent=2, ensure_ascii=False)
    
    total_links = sum(doc['count'] for doc in all_hyperlinks.values())
    print(f"
Total documents: {len(all_hyperlinks)}")
    print(f"Total hyperlinks: {total_links}")
    print(f"Saved to {output_json}")

# Usage
batch_extract_hyperlinks("documents", "all_hyperlinks.json")