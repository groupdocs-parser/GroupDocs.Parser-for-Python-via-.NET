from groupdocs.parser import Parser
from groupdocs.parser.options import HighlightOptions

# Create an instance of Parser class
with Parser("sample.docx") as parser:
    # Define positions to extract highlights from
    positions = [0, 100, 500, 1000]
    
    # Create highlight options (50 characters)
    options = HighlightOptions(50)
    
    for pos in positions:
        # Extract highlight
        highlight = parser.get_highlight(pos, True, options)
        
        if highlight:
            print(f"
Position {pos}:")
            print(f"Text: {highlight.text}")