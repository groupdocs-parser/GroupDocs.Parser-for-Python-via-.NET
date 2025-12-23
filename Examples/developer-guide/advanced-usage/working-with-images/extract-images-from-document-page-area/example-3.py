from groupdocs.parser import Parser
from groupdocs.parser.options import PageAreaOptions, Rectangle, Point, Size

# Create an instance of Parser class
with Parser("document.pptx") as parser:
    if not parser.features.images:
        print("Image extraction not supported")
        return
    
    # Get document info
    info = parser.get_document_info()
    
    # Process specific page (e.g., first page)
    page_index = 0
    
    if page_index < info.page_count:
        # Define area (center of page, 400x300)
        area = Rectangle(Point(100, 100), Size(400, 300))
        options = PageAreaOptions(area)
        
        # Extract images from the area on the specific page
        images = parser.get_images(page_index, options)
        
        if images:
            print(f"Images on page {page_index + 1} in specified area:")
            for image in images:
                print(f"  Type: {image.file_type}")
                print(f"  Position: ({image.rectangle.left}, {image.rectangle.top})")
                print(f"  Size: {image.rectangle.width}x{image.rectangle.height}")