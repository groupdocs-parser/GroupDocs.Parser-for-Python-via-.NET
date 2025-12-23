from groupdocs.parser import Parser
import os

# Create output directory
output_dir = "images_by_page"
os.makedirs(output_dir, exist_ok=True)

# Create an instance of Parser class
with Parser("./sample.pdf") as parser:
    if not parser.features.images:
        print("Image extraction not supported")
        return
    
    # Get document info
    info = parser.get_document_info()
    
    # Process each page
    for page_index in range(info.page_count):
        # Create page-specific directory
        page_dir = os.path.join(output_dir, f"page_{page_index + 1}")
        os.makedirs(page_dir, exist_ok=True)
        
        # Extract images from page
        images = parser.get_images(page_index)
        
        if images:
            for img_idx, image in enumerate(images):
                # Generate filename
                filename = f"image_{img_idx + 1}{image.file_type.extension}"
                filepath = os.path.join(page_dir, filename)
                
                # Save image
                image.save(filepath)
                print(f"Saved: {filepath}")