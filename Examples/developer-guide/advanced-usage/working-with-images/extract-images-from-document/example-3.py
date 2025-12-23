from groupdocs.parser import Parser

# Create an instance of Parser class
with Parser("./sample.pptx") as parser:
    # Check if image extraction is supported
    if not parser.features.images:
        print("Document doesn't support image extraction")
        return
    
    # Extract images
    images = parser.get_images()
    
    if images:
        print(f"Found {len(list(images))} images
")
        
        images = parser.get_images()  # Re-extract as iterator was consumed
        for idx, image in enumerate(images):
            print(f"Image {idx + 1}:")
            print(f"  Page: {image.page.index + 1}")
            print(f"  Format: {image.file_type}")
            print(f"  Rotation: {image.rotation}°")
            print(f"  Rectangle: {image.rectangle}")
            print(f"  Width: {image.rectangle.width}")
            print(f"  Height: {image.rectangle.height}")
            print()