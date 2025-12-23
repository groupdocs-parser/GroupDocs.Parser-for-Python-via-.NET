from groupdocs.parser import Parser

with Parser("./sample.docx") as parser:
  text_reader = parser.get_text()