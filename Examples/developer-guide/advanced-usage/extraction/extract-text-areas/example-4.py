from groupdocs.parser import Parser

# Create an instance of Parser class
with Parser("./sample.docx") as parser:
    # Extract text areas
    text_areas = parser.get_text_areas()
    
    if text_areas is None:
        print("Text areas extraction isn't supported")
    else:
        # Iterate over text areas
        for area in text_areas:
            # Get text style if available
            if area.text_style:
                print(f"Text: {area.text}")
                print(f"Font: {area.text_style.name}")
                print(f"Size: {area.text_style.font_size}")
                print(f"Bold: {area.text_style.is_bold}")
                print(f"Italic: {area.text_style.is_italic}")
                print("---")