from groupdocs.parser import Parser
from groupdocs.parser.options import PageAreaOptions, Rectangle, Point, Size
import re

def extract_links_by_area_and_pattern(file_path, area_rect, url_pattern):
    """
    Extract links from area matching URL pattern.
    
    Args:
        file_path: Path to document
        area_rect: Tuple (x, y, width, height)
        url_pattern: Regex pattern for URLs
    """
    x, y, w, h = area_rect
    area = Rectangle(Point(x, y), Size(w, h))
    options = PageAreaOptions(area)
    
    with Parser(file_path) as parser:
        if not parser.features.hyperlinks:
            print("Hyperlink extraction not supported")
            return []
        
        hyperlinks = parser.get_hyperlinks(options)
        
        if not hyperlinks:
            return []
        
        # Filter by URL pattern
        matching_links = []
        pattern = re.compile(url_pattern, re.IGNORECASE)
        
        for link in hyperlinks:
            if link.url and pattern.search(link.url):
                matching_links.append({
                    'text': link.text,
                    'url': link.url
                })
        
        return matching_links

# Usage - extract PDF links from sidebar
sidebar_area = (400, 100, 200, 700)
pdf_links = extract_links_by_area_and_pattern(
    "document.html",
    sidebar_area,
    r'\.pdf$'
)

print(f"PDF download links in sidebar: {len(pdf_links)}
")
for link in pdf_links:
    print(f"  {link['text']}: {link['url']}")