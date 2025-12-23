from groupdocs.parser import Parser

def extract_images():
    # Create an instance of Parser class
    with Parser("./sample.pdf") as parser:
        # Extract images
        images = parser.get_images()
        
        if images is not None:
            for i, image in enumerate(images):
                # Save image to file
                with open(f"image_{i}.{image.file_type.extension}", "wb") as file:
                    file.write(image.get_image_stream().read())

if __name__ == "__main__":
    extract_images()