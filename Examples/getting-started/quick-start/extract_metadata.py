from groupdocs.parser import Parser

def extract_metadata():
    # Create an instance of Parser class
    with Parser("./sample.pdf") as parser:
        # Extract metadata
        metadata = parser.get_metadata()
        
        if metadata is not None:
            for item in metadata:
                print(f"{item.name}: {item.value}")

if __name__ == "__main__":
    extract_metadata()