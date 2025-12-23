from groupdocs.parser import Parser

# Create an instance of Parser class
with Parser("mixed_files.zip") as parser:
    # Get container items
    attachments = parser.get_container()
    
    if attachments:
        print("Archive Contents:\n")
        
        # Group files by type
        files_by_type = {}
        
        for attachment in attachments:
            # Get file info
            try:
                with attachment.open_parser() as file_parser:
                    info = file_parser.get_document_info()
                    file_type = info.file_type.extension if info and info.file_type else "unknown"
                    
                    if file_type not in files_by_type:
                        files_by_type[file_type] = []
                    
                    files_by_type[file_type].append(attachment.name)
            
            except:
                if "unknown" not in files_by_type:
                    files_by_type["unknown"] = []
                files_by_type["unknown"].append(attachment.name)
        
        # Print summary
        for file_type, files in sorted(files_by_type.items()):
            print(f"
{file_type.upper()} files ({len(files)}):")
            for filename in files:
                print(f"  - {filename}")