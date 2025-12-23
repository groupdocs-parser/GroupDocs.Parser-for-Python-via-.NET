from groupdocs.parser import Parser
from groupdocs.parser.options import ImageOptions, ImageFormat
import os

# Create output directory
output_dir = "images_multi_format"
os.makedirs(output_dir, exist_ok=True)

# Create an instance of Parser class
with Parser("document.docx") as parser:
    images = parser.get_images()
    
    if images:
        # Define formats to save
        formats = {
            'png': ImageOptions(ImageFormat.PNG),
            'jpg': ImageOptions(ImageFormat.JPEG),
            'bmp': ImageOptions(ImageFormat.BMP)
        }
        
        for idx, image in enumerate(images):
            print(f"
Processing image {idx + 1}:")
            
            # Save in each format
            for format_name, options in formats.items():
                filename = f"image_{idx + 1}.{format_name}"
                filepath = os.path.join(output_dir, filename)
                
                image.save(filepath, options)
                print(f"  Saved as {format_name.upper()}")