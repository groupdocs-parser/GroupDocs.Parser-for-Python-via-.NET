from groupdocs.parser import Parser

with Parser("brochure.pdf") as parser:
    images = parser.get_images()
    if images is None:
        print("Image extraction isn't supported for this format.")
    else:
        for image_area in images:
            with image_area.get_image_stream() as stream:
                data = stream.read()
                print(f"Read {len(data)} bytes from page {image_area.page.index + 1}")