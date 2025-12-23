from groupdocs.parser import Parser

def extract_text_from_pdf():
    with Parser("./sample.pdf") as parser:
        text_reader = parser.get_text()
        if text_reader:
            print(text_reader)

if __name__ == "__main__":
    extract_text_from_pdf()