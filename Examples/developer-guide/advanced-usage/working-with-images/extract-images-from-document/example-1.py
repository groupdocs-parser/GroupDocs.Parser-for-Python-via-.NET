from groupdocs.parser import Parser

# Create an instance of Parser class
with Parser("./sample.pdf") as parser:
    # Extract images
    images = parser.get_images()
    
    # Check if image extraction is supported
    if images is None:
        print("Image extraction isn't supported")
    else:
        # Iterate over images
        for idx, image in enumerate(images):
            # Print image information
            print(f"Image {idx + 1}:")
            print(f"  Page: {image.page.index + 1}")
            print(f"  Type: {image.file_type}")
            print(f"  Size: {image.rectangle.width}x{image.rectangle.height}")
            print(f"  Position: ({image.rectangle.left}, {image.rectangle.top})")