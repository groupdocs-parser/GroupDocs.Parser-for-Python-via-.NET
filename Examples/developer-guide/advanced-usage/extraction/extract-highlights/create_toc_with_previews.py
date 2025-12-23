from groupdocs.parser import Parser
from groupdocs.parser.options import HighlightOptions

def create_toc_with_previews(file_path, preview_length=60):
    """
    Create table of contents with text previews for each section.
    """
    with Parser(file_path) as parser:
        # Get TOC
        toc_items = parser.get_toc()
        
        if not toc_items:
            print("TOC extraction not supported")
            return []
        
        toc_with_previews = []
        options = HighlightOptions(preview_length)
        
        # Get text to find section positions
        text_reader = parser.get_text()
        if not text_reader:
            return []
        
        full_text = text_reader
        
        for item in toc_items:
            # Try to extract highlight for this TOC item
            # Use text search to find the section
            section_text = item.text
            position = full_text.find(section_text)
            
            if position >= 0:
                highlight = parser.get_highlight(position, True, options)
                preview = highlight.text if highlight else "No preview available"
            else:
                preview = "Section not found"
            
            toc_with_previews.append({
                'title': item.text,
                'depth': item.depth,
                'preview': preview
            })
        
        return toc_with_previews

# Usage
toc = create_toc_with_previews("SampleWithToc.pdf", preview_length=100)
for item in toc:
    indent = "  " * item['depth']
    print(f"{indent}{item['title']}")
    print(f"{indent}  Preview: {item['preview'][:50]}...")