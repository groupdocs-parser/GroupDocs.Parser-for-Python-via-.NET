from groupdocs.parser import Parser
from groupdocs.parser.options import PageAreaOptions, Rectangle, Point, Size

# Create an instance of Parser class
with Parser("./sample.pdf") as parser:
    # Check if image extraction is supported
    if not parser.features.images:
        print("Image extraction not supported")
        return
    
    # Define the area (upper-left corner, 300x100 pixels)
    area = Rectangle(Point(0, 0), Size(300, 100))
    
    # Create options for the area
    options = PageAreaOptions(area)
    
    # Extract images from the specified area
    images = parser.get_images(options)
    
    if images:
        print(f"Images found in area:")
        for idx, image in enumerate(images):
            print(f"  Image {idx + 1}: {image.file_type}, Page {image.page.index + 1}")
    else:
        print("No images found in the specified area")