from groupdocs.parser import Parser

def process_with_progress(file_path):
    """
    Process container items with progress tracking.
    """
    with Parser(file_path) as parser:
        attachments = parser.get_container()
        
        if attachments is None:
            print("Container extraction not supported")
            return
        
        # Convert to list to get total count
        items = list(attachments)
        total = len(items)
        
        print(f"Processing {total} items...
")
        
        for idx, attachment in enumerate(items, 1):
            # Show progress
            progress = (idx / total) * 100
            print(f"[{progress:5.1f}%] Processing: {attachment.name}")
            
            # Process item (example: just count size)
            # In real scenario, you might extract text, etc.
            
            # Simulate processing
            # time.sleep(0.1)
        
        print("\nProcessing complete!")

# Usage
process_with_progress("archive.zip")