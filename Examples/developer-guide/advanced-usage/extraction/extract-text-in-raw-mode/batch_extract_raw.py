from groupdocs.parser import Parser
from groupdocs.parser.options import TextOptions
from pathlib import Path
import time

def batch_extract_raw(input_dir, output_dir):
    """
    Extract text from multiple documents using Raw mode for speed.
    """
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    extensions = ['.pdf', '.docx', '.doc', '.txt']
    
    start_time = time.time()
    processed_count = 0
    
    # Create raw mode options
    options = TextOptions(False)
    
    for file_path in Path(input_dir).rglob('*'):
        if file_path.suffix.lower() in extensions:
            print(f"Processing: {file_path.name}")
            
            try:
                with Parser(str(file_path)) as parser:
                    text_reader = parser.get_text(options)
                    
                    if text_reader:
                        # Save extracted text
                        output_file = output_path / f"{file_path.stem}.txt"
                        with open(output_file, 'w', encoding='utf-8') as f:
                            f.write(text_reader)
                        
                        processed_count += 1
                
            except Exception as e:
                print(f"  Error: {e}")
    
    elapsed_time = time.time() - start_time
    print(f"
Processed {processed_count} documents in {elapsed_time:.2f} seconds")
    print(f"Average: {elapsed_time/processed_count:.2f} seconds per document")

# Usage
batch_extract_raw("input_documents", "extracted_text")