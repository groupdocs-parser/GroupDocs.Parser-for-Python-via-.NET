from groupdocs.parser import Parser

def extract_hyperlinks_from_range(file_path, start_page, end_page):
    """
    Extract hyperlinks from a range of pages.
    
    Args:
        file_path: Path to document
        start_page: Starting page number (1-based)
        end_page: Ending page number (1-based, inclusive)
    """
    with Parser(file_path) as parser:
        if not parser.features.hyperlinks:
            print("Hyperlink extraction not supported")
            return []
        
        info = parser.get_document_info()
        
        # Validate range
        start_idx = max(0, start_page - 1)
        end_idx = min(info.page_count - 1, end_page - 1)
        
        all_links = []
        
        for page_index in range(start_idx, end_idx + 1):
            hyperlinks = parser.get_hyperlinks(page_index)
            
            if hyperlinks:
                for link in hyperlinks:
                    all_links.append({
                        'page': page_index + 1,
                        'text': link.text,
                        'url': link.url
                    })
        
        return all_links

# Usage - extract hyperlinks from pages 1-5
links = extract_hyperlinks_from_range("document.pdf", 1, 5)
print(f"Found {len(links)} hyperlinks in pages 1-5
")

for link in links:
    print(f"Page {link['page']}: {link['text']} -> {link['url']}")