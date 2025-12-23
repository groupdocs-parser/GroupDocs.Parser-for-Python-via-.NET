from groupdocs.parser import Parser
import os

# Create an instance of Parser class
with Parser("./sample.docx") as parser:
    if not parser.features.images:
        print("Image extraction not supported")
        return
    
    # Define pages to process (e.g., pages 1, 3, and 5)
    pages_to_process = [0, 2, 4]  # Zero-based indices
    
    output_dir = "selected_page_images"
    os.makedirs(output_dir, exist_ok=True)
    
    for page_index in pages_to_process:
        print(f"
Processing page {page_index + 1}...")
        
        # Extract images from this page
        images = parser.get_images(page_index)
        
        if images:
            for img_idx, image in enumerate(images):
                filename = f"page{page_index + 1}_img{img_idx + 1}{image.file_type.extension}"
                filepath = os.path.join(output_dir, filename)
                image.save(filepath)
                print(f"  Saved: {filename}")
        else:
            print(f"  No images found on page {page_index + 1}")