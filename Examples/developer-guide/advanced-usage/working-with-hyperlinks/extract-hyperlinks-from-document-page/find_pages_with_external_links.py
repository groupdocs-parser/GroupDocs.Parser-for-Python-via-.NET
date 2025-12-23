from groupdocs.parser import Parser

def find_pages_with_external_links(file_path):
    """
    Find all pages containing external (http/https) links.
    """
    with Parser(file_path) as parser:
        if not parser.features.hyperlinks:
            print("Hyperlink extraction not supported")
            return []
        
        info = parser.get_document_info()
        pages_with_external_links = []
        
        for page_index in range(info.page_count):
            hyperlinks = parser.get_hyperlinks(page_index)
            
            if hyperlinks:
                has_external = False
                external_links = []
                
                for link in hyperlinks:
                    if link.url and (link.url.startswith('http://') or link.url.startswith('https://')):
                        has_external = True
                        external_links.append(link.url)
                
                if has_external:
                    pages_with_external_links.append({
                        'page': page_index + 1,
                        'links': external_links
                    })
        
        return pages_with_external_links

# Usage
pages = find_pages_with_external_links("article.pdf")

print(f"Pages with external links: {len(pages)}
")
for page_info in pages:
    print(f"Page {page_info['page']}: {len(page_info['links'])} external links")
    for url in page_info['links'][:3]:  # Show first 3
        print(f"  - {url}")