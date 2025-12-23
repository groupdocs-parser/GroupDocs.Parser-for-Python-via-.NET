from groupdocs.parser import Parser

with Parser("./sample.pdf") as parser:
    metadata_items = parser.get_metadata()
    if metadata_items is None:
        print("Metadata extraction is not supported for this format.")
    else:
        for item in metadata_items:
            print(f"{item.name}: {item.value}")