from groupdocs.parser import Parser
from groupdocs.parser.options import LoadOptions

with open("resources/protected.pdf", "rb") as stream:
    options = LoadOptions("secret-password")
    with Parser(stream, options) as parser:
        reader = parser.get_text()
        print(reader if reader else "Text extraction isn't supported.")