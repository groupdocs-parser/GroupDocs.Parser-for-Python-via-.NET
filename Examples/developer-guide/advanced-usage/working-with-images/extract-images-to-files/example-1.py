from groupdocs.parser import Parser
import os

# Create output directory
output_dir = "extracted_images"
os.makedirs(output_dir, exist_ok=True)

# Create an instance of Parser class
with Parser("./document.pdf") as parser:
    # Extract images
    images = parser.get_images()
    
    # Check if image extraction is supported
    if images is None:
        print("Image extraction isn't supported")
    else:
        # Iterate over images and save them
        for idx, image in enumerate(images):
            # Generate filename with appropriate extension
            filename = f"image_{idx + 1}{image.file_type.extension}"
            filepath = os.path.join(output_dir, filename)
            
            # Save image to file
            image.save(filepath)
            print(f"Saved: {filename}")