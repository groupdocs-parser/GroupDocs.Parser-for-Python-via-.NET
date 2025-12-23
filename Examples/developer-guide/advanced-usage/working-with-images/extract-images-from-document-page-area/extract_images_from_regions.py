from groupdocs.parser import Parser
from groupdocs.parser.options import PageAreaOptions, Rectangle, Point, Size
import os

def extract_images_from_regions(file_path, regions, output_dir):
    """
    Extract images from multiple predefined regions.
    
    Args:
        file_path: Path to document
        regions: List of tuples (x, y, width, height)
        output_dir: Directory to save images
    """
    os.makedirs(output_dir, exist_ok=True)
    
    with Parser(file_path) as parser:
        if not parser.features.images:
            print("Image extraction not supported")
            return
        
        for region_idx, (x, y, w, h) in enumerate(regions):
            print(f"
Processing region {region_idx + 1}: ({x}, {y}, {w}x{h})")
            
            # Create rectangle for this region
            area = Rectangle(Point(x, y), Size(w, h))
            options = PageAreaOptions(area)
            
            # Extract images from this region
            images = parser.get_images(options)
            
            if images:
                for img_idx, image in enumerate(images):
                    filename = f"region{region_idx + 1}_img{img_idx + 1}{image.file_type.extension}"
                    filepath = os.path.join(output_dir, filename)
                    image.save(filepath)
                    print(f"  Saved: {filename}")

# Define regions (e.g., header, body, footer)
regions = [
    (0, 0, 600, 100),      # Header region
    (0, 100, 600, 700),    # Body region
    (0, 800, 600, 100)     # Footer region
]

# Extract images from regions
extract_images_from_regions("document.pdf", regions, "region_images")