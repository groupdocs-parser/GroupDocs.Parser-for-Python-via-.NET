from groupdocs.parser import Parser
import os

def extract_specific_files(archive_path, output_dir, extensions=None):
    """
    Extract specific files from ZIP archive based on extension.
    
    Args:
        archive_path: Path to ZIP archive
        output_dir: Directory to save extracted files
        extensions: List of extensions to extract (e.g., ['.pdf', '.docx'])
    """
    os.makedirs(output_dir, exist_ok=True)
    
    with Parser(archive_path) as parser:
        attachments = parser.get_container()
        
        if not attachments:
            print("No files found in archive")
            return
        
        extracted_count = 0
        
        for attachment in attachments:
            # Check extension filter
            if extensions:
                file_ext = os.path.splitext(attachment.name)[1].lower()
                if file_ext not in extensions:
                    continue
            
            print(f"Extracting: {attachment.name}")
            
            try:
                # Open parser for the file
                with attachment.open_parser() as file_parser:
                    # Extract text
                    text_reader = file_parser.get_text()
                    
                    if text_reader:
                        # Save to output directory
                        output_file = os.path.join(output_dir, f"{attachment.name}.txt")
                        
                        with open(output_file, 'w', encoding='utf-8') as f:
                            f.write(text_reader)
                        
                        extracted_count += 1
                        print(f"  Saved to: {output_file}")
            
            except Exception as e:
                print(f"  Error: {e}")
        
        print(f"
Extracted {extracted_count} files")

# Usage - extract only PDF and DOCX files
extract_specific_files("documents.zip", "extracted", ['.pdf', '.docx'])