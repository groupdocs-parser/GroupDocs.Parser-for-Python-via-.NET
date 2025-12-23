from groupdocs.parser import Parser
from groupdocs.parser.exceptions import UnsupportedDocumentFormatException

try:
    with Parser("./unknown.xyz") as parser:
        reader = parser.get_text()
        print(reader if reader else "No text available.")
except Exception as e:
    print(e)