from groupdocs.parser.options import FileType

# Get all supported file types
supported_file_types = FileType.get_supported_file_types()

# Define format categories
word_formats = [".doc", ".docx", ".docm", ".dot", ".dotx", ".dotm", ".odt", ".ott", ".rtf"]
excel_formats = [".xls", ".xlsx", ".xlsm", ".xlsb", ".xlt", ".xltx", ".xltm", ".ods"]
pdf_formats = [".pdf"]

print("Word Processing Formats:")
for file_type in supported_file_types:
    if file_type.extension.lower() in word_formats:
        print(f"  {file_type.extension} - {file_type.file_format}")

print("Spreadsheet Formats:")
for file_type in supported_file_types:
    if file_type.extension.lower() in excel_formats:
        print(f"  {file_type.extension} - {file_type.file_format}")

print("PDF Formats:")
for file_type in supported_file_types:
    if file_type.extension.lower() in pdf_formats:
        print(f"  {file_type.extension} - {file_type.file_format}")