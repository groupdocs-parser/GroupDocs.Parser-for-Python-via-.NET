from groupdocs.parser.options import FileType

# Get all supported file types
supported_file_types = FileType.get_supported_file_types()

# Iterate through the collection
for file_type in sorted(supported_file_types, key=lambda x: x.extension):
    print(f"{file_type.extension} - {file_type.file_format}")

print(f"
Total supported formats: {len(list(supported_file_types))}")