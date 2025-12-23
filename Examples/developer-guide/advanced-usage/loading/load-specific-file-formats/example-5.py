from groupdocs.parser.options import FileFormat

# Common document formats (auto-detected)
# - PDF
# - DOC, DOCX
# - XLS, XLSX
# - PPT, PPTX
# - TXT
# - etc.

# Formats that may require explicit specification:
formats_needing_specification = {
    "Markdown": FileFormat.MARKUP,
    "MHTML": FileFormat.MHTML,
    "OTP": FileFormat.OTP,
}

for name, format_value in formats_needing_specification.items():
    print(f"{name}: {format_value}")