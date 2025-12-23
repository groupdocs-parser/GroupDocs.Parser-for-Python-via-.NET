from groupdocs.parser import Parser

def compare_metadata(file1, file2):
    """
    Compare metadata between two documents.
    """
    def get_metadata_dict(file_path):
        with Parser(file_path) as parser:
            metadata = parser.get_metadata()
            if metadata:
                return {item.name: item.value for item in metadata}
            return {}
    
    metadata1 = get_metadata_dict(file1)
    metadata2 = get_metadata_dict(file2)
    
    # Find common and unique fields
    all_fields = set(metadata1.keys()) | set(metadata2.keys())
    common_fields = set(metadata1.keys()) & set(metadata2.keys())
    
    print(f"Comparing: {file1} vs {file2}
")
    print(f"{'Field':<20} {'File 1':<30} {'File 2':<30} {'Match':<10}")
    print("-" * 95)
    
    for field in sorted(all_fields):
        val1 = str(metadata1.get(field, "N/A"))[:30]
        val2 = str(metadata2.get(field, "N/A"))[:30]
        match = "Yes" if field in common_fields and metadata1.get(field) == metadata2.get(field) else "No"
        
        print(f"{field:<20} {val1:<30} {val2:<30} {match:<10}")

# Usage
compare_metadata("version1.docx", "version2.docx")