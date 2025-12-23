from groupdocs.parser import Parser
from groupdocs.parser.exceptions import UnsupportedDocumentFormatException

with Parser("./archive.zip") as parser:
    attachments = parser.get_container()
    if attachments is None:
        print("Container extraction isn't supported for this format.")
    else:
        for item in attachments:
            print(item.file_path)
            try:
                with item.open_parser() as attachment_parser:
                    reader = attachment_parser.get_text()
                    print(reader if reader else "No text available.")
            except Exception as e:
                print(e)