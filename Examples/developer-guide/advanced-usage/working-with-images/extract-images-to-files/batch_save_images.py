from groupdocs.parser import Parser
from pathlib import Path
import os

def batch_save_images(input_dir, output_dir):
    """
    Extract and save images from all documents in a directory.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    extensions = ['.pdf', '.docx', '.doc', '.pptx', '.ppt']
    
    for file_path in Path(input_dir).rglob('*'):
        if file_path.suffix.lower() in extensions:
            print(f"
Processing: {file_path.name}")
            
            # Create subdirectory for this document
            doc_output_dir = os.path.join(output_dir, file_path.stem)
            os.makedirs(doc_output_dir, exist_ok=True)
            
            try:
                with Parser(str(file_path)) as parser:
                    images = parser.get_images()
                    
                    if images:
                        image_count = 0
                        for idx, image in enumerate(images):
                            filename = f"image_{idx + 1}{image.file_type.extension}"
                            filepath = os.path.join(doc_output_dir, filename)
                            image.save(filepath)
                            image_count += 1
                        
                        print(f"  Saved {image_count} images")
                    else:
                        print(f"  No images or not supported")
            
            except Exception as e:
                print(f"  Error: {e}")

# Usage
batch_save_images("input_documents", "all_extracted_images")