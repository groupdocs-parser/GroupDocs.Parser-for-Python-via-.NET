from groupdocs.parser import Parser
import os

def process_files_from_directory(directory_path):
    """Process all supported documents in a directory"""
    
    # Get all files in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        # Skip if not a file
        if not os.path.isfile(file_path):
            continue
        
        try:
            print(f"
Processing: {filename}")
            
            # Create parser instance
            with Parser(file_path) as parser:
                # Get document info
                doc_info = parser.get_document_info()
                print(f"  Type: {doc_info.file_type.file_format}")
                print(f"  Pages: {doc_info.page_count}")
                
                # Extract text
                text_reader = parser.get_text()
                if text_reader:
                    text = text_reader
                    print(f"  Characters: {len(text)}")
                    
        except Exception as e:
            print(f"  Error: {e}")