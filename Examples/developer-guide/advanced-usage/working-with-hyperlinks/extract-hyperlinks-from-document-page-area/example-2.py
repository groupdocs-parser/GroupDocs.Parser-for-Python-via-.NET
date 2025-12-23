from groupdocs.parser import Parser
from groupdocs.parser.options import PageAreaOptions, Rectangle, Point, Size

# Create an instance of Parser class
with Parser("document.pdf") as parser:
    if not parser.features.hyperlinks:
        print("Hyperlink extraction not supported")
        sys.exit()
    
    # Define area (sidebar region)
    area = Rectangle(Point(400, 0), Size(200, 800))
    options = PageAreaOptions(area)
    
    # Get document info
    info = parser.get_document_info()
    
    # Process first page
    page_index = 0
    
    if page_index < info.page_count:
        # Extract hyperlinks from area on specific page
        hyperlinks = parser.get_hyperlinks(page_index, options)
        
        if hyperlinks:
            print(f"Hyperlinks in sidebar (page {page_index + 1}):")
            for link in hyperlinks:
                print(f"  {link.text}: {link.url}")