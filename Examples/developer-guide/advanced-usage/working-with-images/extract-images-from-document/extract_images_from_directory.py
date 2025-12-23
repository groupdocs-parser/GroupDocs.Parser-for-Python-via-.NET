from groupdocs.parser import Parser
import os
from pathlib import Path

def extract_images_from_directory(input_dir, output_dir):
    """
    Extract images from all documents in a directory.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Supported document extensions
    extensions = ['.pdf', '.docx', '.doc', '.xlsx', '.pptx', '.ppt']
    
    for file_path in Path(input_dir).rglob('*'):
        if file_path.suffix.lower() in extensions:
            print(f"
Processing: {file_path.name}")
            
            try:
                with Parser(str(file_path)) as parser:
                    images = parser.get_images()
                    
                    if images is None:
                        print(f"  Image extraction not supported")
                        continue
                    
                    # Create subdirectory for this document
                    doc_output_dir = os.path.join(output_dir, file_path.stem)
                    os.makedirs(doc_output_dir, exist_ok=True)
                    
                    # Save images
                    image_count = 0
                    for idx, image in enumerate(images):
                        filename = f"image_{idx + 1}{image.file_type.extension}"
                        filepath = os.path.join(doc_output_dir, filename)
                        image.save(filepath)
                        image_count += 1
                    
                    print(f"  Extracted {image_count} images")
                    
            except Exception as e:
                print(f"  Error: {e}")

# Usage
extract_images_from_directory("input_documents", "extracted_images")