from groupdocs.parser import Parser
from groupdocs.parser.options import HighlightOptions

def create_document_preview(file_path, num_sections=5, section_length=100):
    """
    Create a document preview by extracting highlights from various positions.
    """
    with Parser(file_path) as parser:
        # Get document text to determine positions
        text_reader = parser.get_text()
        
        if not text_reader:
            print("Text extraction not supported")
            return None
        
        full_text = text_reader
        text_length = len(full_text)
        
        # Calculate evenly distributed positions
        if text_length <= section_length:
            positions = [0]
        else:
            step = text_length // num_sections
            positions = [i * step for i in range(num_sections)]
        
        # Extract highlights
        preview_sections = []
        options = HighlightOptions(section_length)
        
        for pos in positions:
            highlight = parser.get_highlight(pos, True, options)
            if highlight:
                preview_sections.append(highlight.text)
        
        return {
            'document_length': text_length,
            'preview_sections': preview_sections,
            'full_preview': '
...
'.join(preview_sections)
        }

# Usage
preview = create_document_preview("sample.pdf", num_sections=3, section_length=150)

if preview:
    print(f"Document length: {preview['document_length']} characters
")
    print("Preview:")
    print(preview['full_preview'])