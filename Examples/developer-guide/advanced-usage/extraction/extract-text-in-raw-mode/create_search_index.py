from groupdocs.parser import Parser
from groupdocs.parser.options import TextOptions
from pathlib import Path
import json

def create_search_index(input_dir, index_file):
    """
    Create a search index from documents using Raw mode.
    """
    index = {}
    options = TextOptions(False)  # Raw mode for speed
    
    for file_path in Path(input_dir).rglob('*'):
        if file_path.suffix.lower() in ['.pdf', '.docx', '.doc', '.txt']:
            try:
                with Parser(str(file_path)) as parser:
                    text_reader = parser.get_text(options)
                    
                    if text_reader:
                        text = text_reader
                        
                        # Create index entry
                        index[str(file_path)] = {
                            'filename': file_path.name,
                            'size': len(text),
                            'preview': text[:200],  # First 200 chars
                            'word_count': len(text.split())
                        }
                        
                        print(f"Indexed: {file_path.name}")
            
            except Exception as e:
                print(f"Error indexing {file_path.name}: {e}")
    
    # Save index
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    
    print(f"
Created index with {len(index)} documents")
    return index

# Usage
index = create_search_index("documents", "search_index.json")