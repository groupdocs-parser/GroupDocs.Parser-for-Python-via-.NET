from groupdocs.parser import Parser

def get_document_information():
    # Create an instance of Parser class
    with Parser("./sample.pdf") as parser:
        # Get document info
        info = parser.get_document_info()
        
        print(f"File type: {info.file_type.file_format}")
        print(f"Page count: {info.page_count}")
        print(f"Size: {info.size} bytes")

if __name__ == "__main__":
    get_document_information()