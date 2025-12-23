from groupdocs.parser import Parser
from groupdocs.parser.options import PageTextAreaOptions, Rectangle, Point, Size

def extract_from_regions(file_path, regions):
    """
    Extract text from specific regions of a document.
    
    Args:
        file_path: Path to the document
        regions: List of tuples (x, y, width, height)
    """
    with Parser(file_path) as parser:
        if not parser.features.text_areas:
            print("Text areas extraction not supported")
            return {}
        
        results = {}
        
        for idx, (x, y, w, h) in enumerate(regions):
            # Create rectangle for this region
            rect = Rectangle(Point(x, y), Size(w, h))
            options = PageTextAreaOptions(None, rect)
            
            # Extract text areas from this region
            areas = parser.get_text_areas(options)
            
            # Collect text from all areas in this region
            text_list = [area.text for area in areas] if areas else []
            results[f"region_{idx}"] = " ".join(text_list)
        
        return results

# Define regions (e.g., header, body, footer)
regions = [
    (0, 0, 600, 100),      # Header region
    (0, 100, 600, 700),    # Body region
    (0, 800, 600, 100)     # Footer region
]

# Extract text from regions
extracted = extract_from_regions("sample.pdf", regions)
for region_name, text in extracted.items():
    print(f"{region_name}: {text[:100]}...")