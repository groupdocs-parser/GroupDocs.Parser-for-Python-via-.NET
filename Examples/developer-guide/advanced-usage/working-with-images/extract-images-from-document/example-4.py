from groupdocs.parser import Parser
from groupdocs.parser.options import ImageOptions, ImageFormat

# Create an instance of Parser class
with Parser("./sample.pdf") as parser:
    # Extract images
    images = parser.get_images()
    
    if images:
        for idx, image in enumerate(images):
            # Get image stream
            image_stream = image.get_image_stream()
            
            # Read image data
            image_data = image_stream.read()
            print(f"Image {idx + 1}: {len(image_data)} bytes, format: {image.file_type}")
            
            # Optionally convert to PNG
            png_options = ImageOptions(ImageFormat.PNG)
            png_stream = image.get_image_stream(png_options)
            png_data = png_stream.read()
            print(f"  Converted to PNG: {len(png_data)} bytes")