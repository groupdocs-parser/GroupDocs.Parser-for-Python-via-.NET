from groupdocs.parser import Parser
from groupdocs.parser.options import PageAreaOptions, Rectangle, Point, Size

def extract_links_from_regions(file_path, regions):
    """
    Extract hyperlinks from multiple regions.
    
    Args:
        file_path: Path to document
        regions: Dict of region names to (x, y, width, height) tuples
    """
    with Parser(file_path) as parser:
        if not parser.features.hyperlinks:
            print("Hyperlink extraction not supported")
            return {}
        
        results = {}
        
        for region_name, (x, y, w, h) in regions.items():
            # Create rectangle for this region
            area = Rectangle(Point(x, y), Size(w, h))
            options = PageAreaOptions(area)
            
            # Extract hyperlinks from this region
            hyperlinks = parser.get_hyperlinks(options)
            
            if hyperlinks:
                results[region_name] = [link.url for link in hyperlinks]
            else:
                results[region_name] = []
        
        return results

# Define regions
regions = {
    'header': (0, 0, 600, 100),
    'sidebar': (0, 100, 150, 700),
    'footer': (0, 800, 600, 100)
}

# Extract links from regions
links_by_region = extract_links_from_regions("page.html", regions)

for region, urls in links_by_region.items():
    print(f"{region.upper()}: {len(urls)} links")
    for url in urls[:5]:  # Show first 5
        print(f"  - {url}")