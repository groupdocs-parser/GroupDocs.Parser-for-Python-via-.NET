from groupdocs.parser import Parser

# Create an instance of Parser class
with Parser("report.docx") as parser:
    if not parser.features.hyperlinks:
        print("Hyperlink extraction not supported")
        return
    
    # Get document info
    info = parser.get_document_info()
    
    if info.page_count == 0:
        print("Document has no pages")
        return
    
    # Iterate over pages
    total_links = 0
    
    for page_index in range(info.page_count):
        print(f"
=== Page {page_index + 1}/{info.page_count} ===")
        
        # Extract hyperlinks from current page
        hyperlinks = parser.get_hyperlinks(page_index)
        
        if hyperlinks:
            page_links = list(hyperlinks)
            print(f"Found {len(page_links)} hyperlinks:")
            
            for link in page_links:
                print(f"  • {link.text} -> {link.url}")
            
            total_links += len(page_links)
        else:
            print("No hyperlinks on this page")
    
    print(f"
Total hyperlinks: {total_links}")