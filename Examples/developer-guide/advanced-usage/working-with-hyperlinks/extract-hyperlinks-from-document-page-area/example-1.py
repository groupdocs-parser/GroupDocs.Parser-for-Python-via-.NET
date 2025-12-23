from groupdocs.parser import Parser
from groupdocs.parser.options import PageAreaOptions, Rectangle, Point, Size

# Create an instance of Parser class
with Parser("./webpage.html") as parser:
    # Check if hyperlink extraction is supported
    if not parser.features.hyperlinks:
        print("Hyperlink extraction not supported")
        sys.exit()
    
    # Define the area (upper portion, 600x200 pixels)
    area = Rectangle(Point(0, 0), Size(600, 200))
    
    # Create options for the area
    options = PageAreaOptions(area)
    
    # Extract hyperlinks from the specified area
    hyperlinks = parser.get_hyperlinks(options)
    
    if hyperlinks:
        print(f"Hyperlinks found in area:")
        for link in hyperlinks:
            print(f"  {link.text} -> {link.url}")
    else:
        print("No hyperlinks found in the specified area")