from groupdocs.parser import Parser
import os

def save_images_by_type(file_path, output_dir, target_extensions):
    """
    Save only images of specific types.
    
    Args:
        file_path: Path to document
        output_dir: Output directory
        target_extensions: List of extensions to save (e.g., ['.jpg', '.png'])
    """
    os.makedirs(output_dir, exist_ok=True)
    
    with Parser(file_path) as parser:
        images = parser.get_images()
        
        if images is None:
            print("Image extraction not supported")
            return
        
        saved_count = 0
        skipped_count = 0
        
        for idx, image in enumerate(images):
            ext = image.file_type.extension.lower()
            
            if ext in target_extensions:
                filename = f"image_{idx + 1}{ext}"
                filepath = os.path.join(output_dir, filename)
                
                image.save(filepath)
                print(f"Saved: {filename}")
                saved_count += 1
            else:
                print(f"Skipped: image_{idx + 1}{ext}")
                skipped_count += 1
        
        print(f"
Saved: {saved_count}, Skipped: {skipped_count}")

# Usage - save only JPG and PNG images
save_images_by_type("document.pdf", "filtered_images", ['.jpg', '.jpeg', '.png'])