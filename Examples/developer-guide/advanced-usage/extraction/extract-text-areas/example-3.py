from groupdocs.parser import Parser
from groupdocs.parser.options import PageTextAreaOptions, Rectangle, Point, Size

# Create an instance of Parser class
with Parser("./sample.pdf") as parser:
    # Define the region (upper-left corner, 300x100 pixels)
    region = Rectangle(Point(0, 0), Size(300, 100))
    
    # Create options to extract only text areas with digits in the specified region
    options = PageTextAreaOptions(r"\d+", region)
    
    # Extract text areas
    text_areas = parser.get_text_areas(options)
    
    if text_areas is None:
        print("Text areas extraction isn't supported")
    else:
        # Iterate over filtered text areas
        for area in text_areas:
            print(f"Page: {area.page.index}, Rectangle: {area.rectangle}, Text: {area.text}")