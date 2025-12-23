from groupdocs.parser import Parser
from groupdocs.parser.options import PageAreaOptions, Rectangle, Point, Size

def extract_footer_links(file_path, page_height=842):
    """
    Extract links from document footer.
    
    Args:
        file_path: Path to document
        page_height: Approximate page height in points (default: A4 = 842)
    """
    with Parser(file_path) as parser:
        if not parser.features.hyperlinks:
            print("Hyperlink extraction not supported")
            return []
        
        # Define footer area (bottom 100 pixels)
        footer_y = page_height - 100
        footer_area = Rectangle(Point(0, footer_y), Size(600, 100))
        options = PageAreaOptions(footer_area)
        
        # Extract hyperlinks from footer
        hyperlinks = parser.get_hyperlinks(options)
        
        if hyperlinks:
            links = []
            for link in hyperlinks:
                links.append({
                    'text': link.text or '',
                    'url': link.url or '',
                    'position': (link.rectangle.left, link.rectangle.top)
                })
            return links
        
        return []

# Usage
footer_links = extract_footer_links("document.pdf")

print(f"Footer links: {len(footer_links)}")
for link in footer_links:
    print(f"{link['text']}: {link['url']}")