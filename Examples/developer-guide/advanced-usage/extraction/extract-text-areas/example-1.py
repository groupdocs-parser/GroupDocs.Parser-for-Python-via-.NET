from groupdocs.parser import Parser

# Create an instance of Parser class
with Parser("./sample.pdf") as parser:
    # Extract text areas
    text_areas = parser.get_text_areas()
    
    # Check if text areas extraction is supported
    if text_areas is None:
        print("Text areas extraction isn't supported")
    else:
        # Iterate over text areas
        for area in text_areas:
            # Print page index, rectangle, and text
            print(f"Page: {area.page.index}, Rectangle: {area.rectangle}, Text: {area.text}")