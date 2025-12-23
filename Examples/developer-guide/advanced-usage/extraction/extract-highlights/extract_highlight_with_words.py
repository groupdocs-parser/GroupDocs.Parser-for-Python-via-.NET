from groupdocs.parser import Parser
from groupdocs.parser.options import HighlightOptions

def extract_highlight_with_words(file_path, position, max_length=100):
    """
    Extract highlight ensuring complete words.
    """
    with Parser(file_path) as parser:
        # Extract more than needed
        options = HighlightOptions(max_length + 50)
        highlight = parser.get_highlight(position, True, options)
        
        if not highlight:
            return None
        
        text = highlight.text
        
        # Find last complete word within max_length
        if len(text) > max_length:
            truncated = text[:max_length]
            last_space = truncated.rfind(' ')
            if last_space > 0:
                text = truncated[:last_space] + "..."
        
        return {
            'position': highlight.position,
            'text': text,
            'complete_words': True
        }

# Usage
highlight = extract_highlight_with_words("sample.pdf", 500, 80)
if highlight:
    print(f"Position {highlight['position']}:")
    print(highlight['text'])