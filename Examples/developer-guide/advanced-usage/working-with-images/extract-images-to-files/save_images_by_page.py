from groupdocs.parser import Parser
import os

def save_images_by_page(file_path, output_dir):
    """
    Save images organized in subdirectories by page.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    with Parser(file_path) as parser:
        images = parser.get_images()
        
        if images is None:
            print("Image extraction not supported")
            return
        
        # Group images by page
        images_by_page = {}
        
        for image in images:
            page_num = image.page.index + 1
            if page_num not in images_by_page:
                images_by_page[page_num] = []
            images_by_page[page_num].append(image)
        
        # Save images organized by page
        total_saved = 0
        
        for page_num, page_images in sorted(images_by_page.items()):
            # Create page directory
            page_dir = os.path.join(output_dir, f"page_{page_num}")
            os.makedirs(page_dir, exist_ok=True)
            
            print(f"
Page {page_num}: {len(page_images)} images")
            
            for img_idx, image in enumerate(page_images):
                filename = f"image_{img_idx + 1}{image.file_type.extension}"
                filepath = os.path.join(page_dir, filename)
                
                image.save(filepath)
                print(f"  Saved: {filename}")
                total_saved += 1
        
        print(f"
Total images saved: {total_saved}")

# Usage
save_images_by_page("multi_page.pdf", "images_by_page")