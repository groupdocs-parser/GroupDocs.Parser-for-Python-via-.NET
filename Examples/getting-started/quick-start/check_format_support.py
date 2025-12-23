from groupdocs.parser import Parser

def check_format_support():
    # Check if file format is supported
    if Parser.get_file_info("./sample.pdf").file_type.file_format != "Unknown":
        print("Format is supported")
        
        # Process the document
        with Parser("./sample.pdf") as parser:
            text_reader = parser.get_text()
            if text_reader is not None:
                print(text_reader)
    else:
        print("Format is not supported")

if __name__ == "__main__":
    check_format_support()