from groupdocs.parser import Parser

# Create an instance of Parser class
with Parser("./sample.pdf") as parser:
    # Check if text areas extraction is supported
    if not parser.features.text_areas:
        print("Document doesn't support text areas extraction")
        return
    
    # Get document info
    info = parser.get_document_info()
    
    # Check if document has pages
    if info.page_count == 0:
        print("Document has no pages")
        return
    
    # Iterate over pages
    for page_index in range(info.page_count):
        print(f"
Page {page_index + 1}/{info.page_count}")
        
        # Extract text areas from the page
        text_areas = parser.get_text_areas(page_index)
        
        # Iterate over text areas
        if text_areas:
            for area in text_areas:
                # Print rectangle and text
                rect = area.rectangle
                print(f"Position: ({rect.left}, {rect.top}), Size: ({rect.width}x{rect.height})")
                print(f"Text: {area.text}")