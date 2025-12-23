from groupdocs.parser import Parser
import os

# Create output directory
output_dir = "first_images"
os.makedirs(output_dir, exist_ok=True)

# Create an instance of Parser class
with Parser("./sample.pdf") as parser:
    if not parser.features.images:
        print("Image extraction not supported")
        return
    
    info = parser.get_document_info()
    
    for page_index in range(info.page_count):
        # Extract images from page
        images = parser.get_images(page_index)
        
        if images:
            # Get first image only
            first_image = next(iter(images), None)
            
            if first_image:
                filename = f"page_{page_index + 1}_first{first_image.file_type.extension}"
                filepath = os.path.join(output_dir, filename)
                first_image.save(filepath)
                print(f"Saved first image from page {page_index + 1}: {filename}")