from groupdocs.parser import Parser

def extract_metadata_example():
    with Parser("./sample.docx") as parser:
        metadata = parser.get_metadata()
        if metadata:
            for item in metadata:
                print(f"{item.name}: {item.value}")

if __name__ == "__main__":
    extract_metadata_example()