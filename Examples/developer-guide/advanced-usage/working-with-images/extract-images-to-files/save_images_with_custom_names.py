from groupdocs.parser import Parser
import os
from datetime import datetime

def save_images_with_custom_names(file_path, output_dir, prefix="doc"):
    """
    Save images with custom naming pattern.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    with Parser(file_path) as parser:
        images = parser.get_images()
        
        if images is None:
            print("Image extraction not supported")
            return 0
        
        saved_count = 0
        
        for idx, image in enumerate(images):
            # Create custom filename
            filename = f"{prefix}_{timestamp}_page{image.page.index + 1}_img{idx + 1}{image.file_type.extension}"
            filepath = os.path.join(output_dir, filename)
            
            # Save image
            image.save(filepath)
            print(f"Saved: {filename}")
            saved_count += 1
        
        return saved_count

# Usage
count = save_images_with_custom_names("report.pdf", "saved_images", prefix="report")
print(f"
Total images saved: {count}")