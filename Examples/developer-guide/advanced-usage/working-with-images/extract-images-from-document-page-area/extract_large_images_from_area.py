from groupdocs.parser import Parser
from groupdocs.parser.options import PageAreaOptions, Rectangle, Point, Size
import os

def extract_large_images_from_area(file_path, area_rect, min_width, min_height, output_dir):
    """
    Extract images larger than specified size from an area.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    with Parser(file_path) as parser:
        if not parser.features.images:
            print("Image extraction not supported")
            return
        
        options = PageAreaOptions(area_rect)
        images = parser.get_images(options)
        
        if not images:
            print("No images found in area")
            return
        
        saved_count = 0
        
        for image in images:
            # Check image size
            if image.rectangle.width >= min_width and image.rectangle.height >= min_height:
                filename = f"large_image_{saved_count + 1}{image.file_type.extension}"
                filepath = os.path.join(output_dir, filename)
                image.save(filepath)
                
                print(f"Saved: {filename} ({image.rectangle.width}x{image.rectangle.height})")
                saved_count += 1
        
        print(f"
Total large images saved: {saved_count}")

# Usage - extract images larger than 100x100 from center area
center_area = Rectangle(Point(100, 100), Size(400, 600))
extract_large_images_from_area("document.pdf", center_area, 100, 100, "large_images")