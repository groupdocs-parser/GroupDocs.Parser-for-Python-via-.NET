from groupdocs.parser import Parser
from groupdocs.parser.options import ImageOptions, ImageFormat
import os

# Create output directory
output_dir = "converted_images"
os.makedirs(output_dir, exist_ok=True)

# Create an instance of Parser class
with Parser("./sample.pdf") as parser:
    # Extract images
    images = parser.get_images()
    
    if images:
        # Create image options for PNG format
        png_options = ImageOptions(ImageFormat.PNG)
        
        for idx, image in enumerate(images):
            # Save image as PNG (regardless of original format)
            filename = f"image_{idx + 1}.png"
            filepath = os.path.join(output_dir, filename)
            
            # Save with conversion
            image.save(filepath, png_options)
            print(f"Saved as PNG: {filepath}")