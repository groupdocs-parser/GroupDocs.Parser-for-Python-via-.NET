from groupdocs.parser import Parser

def extract_text_from_specific_page():
    # Create an instance of Parser class
    with Parser("./sample.pdf") as parser:
        # Get document info to check page count
        info = parser.get_document_info()
        
        if info.page_count > 0:
            # Extract text from the first page (page index is 0-based)
            text_reader = parser.get_text(0)
            
            if text_reader is not None:
                print(text_reader)

if __name__ == "__main__":
    extract_text_from_specific_page()