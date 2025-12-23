from groupdocs.parser import Parser

def extract_images_example():
    with Parser("./sample.pdf") as parser:
        images = parser.get_images()
        if images:
            for i, image in enumerate(images):
                with open(f"image_{i}.png", "wb") as file:
                    image_stream = image.get_image_stream()
                    file.write(image_stream.read())

if __name__ == "__main__":
    extract_images_example()