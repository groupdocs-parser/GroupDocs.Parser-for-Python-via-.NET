from groupdocs.parser import Parser

# Create an instance of Parser class
with Parser("./sample.pdf") as parser:
    # Check if image extraction is supported
    if not parser.features.images:
        print("Document doesn't support image extraction")
        return
    
    # Extract images from page 0 (first page)
    page_index = 0
    images = parser.get_images(page_index)
    
    if images:
        print(f"Images on page {page_index + 1}:")
        for idx, image in enumerate(images):
            print(f"  Image {idx + 1}: {image.file_type}, size: {image.rectangle.width}x{image.rectangle.height}")