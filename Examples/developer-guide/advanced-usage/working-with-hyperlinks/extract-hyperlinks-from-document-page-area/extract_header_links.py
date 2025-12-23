from groupdocs.parser import Parser
from groupdocs.parser.options import PageAreaOptions, Rectangle, Point, Size

def extract_header_links(file_path):
    """
    Extract navigation links from document header.
    """
    with Parser(file_path) as parser:
        if not parser.features.hyperlinks:
            print("Hyperlink extraction not supported")
            return []
        
        # Define header area (top 100 pixels, full width)
        header_area = Rectangle(Point(0, 0), Size(1000, 100))
        options = PageAreaOptions(header_area)
        
        # Extract hyperlinks from header
        hyperlinks = parser.get_hyperlinks(options)
        
        if hyperlinks:
            links = []
            for link in hyperlinks:
                links.append({
                    'text': link.text or 'No text',
                    'url': link.url or ''
                })
            return links
        
        return []

# Usage
nav_links = extract_header_links("website.html")

print(f"Navigation links ({len(nav_links)}):")
for link in nav_links:
    print(f"  {link['text']} → {link['url']}")