from groupdocs.parser import Parser
from groupdocs.parser.exceptions import UnsupportedDocumentFormatException

def print_text(item_path, parser):
    reader = parser.get_text()
    print(f"{item_path}: {reader if reader else '[no text]'}")

with Parser("portfolio.pdf") as parser:
    container = parser.get_container()
    if container is None:
        print("Container extraction isn't supported for this format.")
    else:
        for item in container:
            try:
                with item.open_parser() as inner_parser:
                    print_text(item.file_path, inner_parser)
            except UnsupportedDocumentFormatException:
                print(f"{item.file_path}: format is not supported.")