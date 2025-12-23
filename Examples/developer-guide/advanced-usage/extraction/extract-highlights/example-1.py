from groupdocs.parser import Parser
from groupdocs.parser.options import HighlightOptions

# Create an instance of Parser class
with Parser("./sample.pdf") as parser:
    # Create highlight options (extract 20 characters)
    options = HighlightOptions(20)
    
    # Extract highlight at position 100
    highlight = parser.get_highlight(100, True, options)
    
    if highlight:
        print(f"Position: {highlight.position}")
        print(f"Text: {highlight.text}")
    else:
        print("Highlight extraction not supported or position out of range")