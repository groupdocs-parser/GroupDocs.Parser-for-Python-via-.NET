from groupdocs.parser import Parser
from groupdocs.parser.options import HighlightOptions

def extract_multiple_highlights(file_path, positions, length=50):
    """
    Extract highlights from multiple positions.
    """
    highlights = []
    
    with Parser(file_path) as parser:
        options = HighlightOptions(length)
        
        for position in positions:
            highlight = parser.get_highlight(position, True, options)
            
            if highlight:
                highlights.append({
                    'position': highlight.position,
                    'text': highlight.text,
                    'length': len(highlight.text)
                })
        
        return highlights

# Extract highlights at specific positions
positions = [0, 500, 1000, 1500, 2000]
highlights = extract_multiple_highlights("sample.pdf", positions, length=80)

print(f"Extracted {len(highlights)} highlights:
")
for h in highlights:
    print(f"Position {h['position']}:")
    print(f"  {h['text'][:60]}...")
    print()