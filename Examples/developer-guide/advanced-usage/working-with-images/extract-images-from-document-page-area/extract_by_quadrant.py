from groupdocs.parser import Parser
from groupdocs.parser.options import PageAreaOptions, Rectangle, Point, Size

def extract_by_quadrant(file_path, page_width=600, page_height=800):
    """
    Extract images by document quadrant (TL, TR, BL, BR).
    """
    # Define quadrants
    quadrant_size_w = page_width // 2
    quadrant_size_h = page_height // 2
    
    quadrants = {
        'Top-Left': Rectangle(Point(0, 0), Size(quadrant_size_w, quadrant_size_h)),
        'Top-Right': Rectangle(Point(quadrant_size_w, 0), Size(quadrant_size_w, quadrant_size_h)),
        'Bottom-Left': Rectangle(Point(0, quadrant_size_h), Size(quadrant_size_w, quadrant_size_h)),
        'Bottom-Right': Rectangle(Point(quadrant_size_w, quadrant_size_h), Size(quadrant_size_w, quadrant_size_h))
    }
    
    with Parser(file_path) as parser:
        if not parser.features.images:
            print("Image extraction not supported")
            return
        
        for quadrant_name, area in quadrants.items():
            options = PageAreaOptions(area)
            images = parser.get_images(options)
            
            if images:
                image_list = list(images)
                print(f"{quadrant_name}: {len(image_list)} images")
            else:
                print(f"{quadrant_name}: 0 images")

# Usage
extract_by_quadrant("layout.pdf")