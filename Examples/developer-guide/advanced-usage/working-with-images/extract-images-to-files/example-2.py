from groupdocs.parser import Parser
from groupdocs.parser.options import ImageOptions, ImageFormat
import os

# Create output directory
output_dir = "images_png"
os.makedirs(output_dir, exist_ok=True)

# Create an instance of Parser class
with Parser("presentation.pptx") as parser:
    # Extract images
    images = parser.get_images()
    
    if images is None:
        print("Image extraction not supported")
    else:
        # Create image options for PNG format
        png_options = ImageOptions(ImageFormat.PNG)
        
        # Save all images as PNG
        for idx, image in enumerate(images):
            filename = f"image_{idx + 1}.png"
            filepath = os.path.join(output_dir, filename)
            
            # Save with format conversion
            image.save(filepath, png_options)
            print(f"Saved as PNG: {filename}")