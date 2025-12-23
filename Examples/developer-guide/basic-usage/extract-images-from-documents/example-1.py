from groupdocs.parser import Parser

with Parser("./slides.pptx") as parser:
    images = parser.get_images()
    if images is None:
        print("Image extraction isn't supported for this format.")
    else:
        for index, image_area in enumerate(images, start=1):
            print(f"Page: {image_area.page.index + 1}, Type: {image_area.file_type}")
            # Save each image
            output_path = f"image-{index}.{image_area.file_type.extension}"
            image_area.save(output_path)