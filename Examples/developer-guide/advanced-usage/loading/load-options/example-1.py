from groupdocs.parser import Parser
from groupdocs.parser.options import LoadOptions

options = LoadOptions("secret-password")

with Parser("protected.pdf", options) as parser:
    reader = parser.get_text()
    print(reader if reader else "Text extraction isn't supported.")