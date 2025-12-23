from groupdocs.parser import Parser
from groupdocs.parser.options import PageAreaOptions, Rectangle, Point, Size
import os

def extract_header_logos(file_path, output_dir):
    """
    Extract logo images from document header area.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    with Parser(file_path) as parser:
        if not parser.features.images:
            print("Image extraction not supported")
            return
        
        # Define header area (top 150 pixels, full width)
        header_area = Rectangle(Point(0, 0), Size(1000, 150))
        options = PageAreaOptions(header_area)
        
        # Extract images from header
        images = parser.get_images(options)
        
        if images:
            print(f"Found {len(list(images))} images in header
")
            
            # Re-extract as iterator was consumed
            images = parser.get_images(options)
            
            for idx, image in enumerate(images):
                filename = f"logo_{idx + 1}{image.file_type.extension}"
                filepath = os.path.join(output_dir, filename)
                image.save(filepath)
                print(f"Saved logo: {filename}")
        else:
            print("No images found in header area")

# Usage
extract_header_logos("invoice.pdf", "extracted_logos")