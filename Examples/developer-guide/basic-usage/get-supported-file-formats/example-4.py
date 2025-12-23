from groupdocs.parser.options import FileType

# Get all supported file types
supported_file_types = FileType.get_supported_file_types()

# Display format details
print("Supported Document Formats:\n")
print(f"{'Extension':<12} {'Format Name':<50}")
print("-" * 62)

for file_type in sorted(supported_file_types, key=lambda x: x.extension):
    print(f"{file_type.extension:<12} {file_type.file_format:<50}")