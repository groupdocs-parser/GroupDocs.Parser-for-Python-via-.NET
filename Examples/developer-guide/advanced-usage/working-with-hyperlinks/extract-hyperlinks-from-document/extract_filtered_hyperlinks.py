from groupdocs.parser import Parser

def extract_filtered_hyperlinks(file_path, url_pattern=None, text_pattern=None):
    """
    Extract hyperlinks with optional filtering by URL or text pattern.
    """
    import re
    
    with Parser(file_path) as parser:
        if not parser.features.hyperlinks:
            print("Hyperlink extraction not supported")
            return []
        
        hyperlinks = parser.get_hyperlinks()
        
        if not hyperlinks:
            return []
        
        filtered_links = []
        
        for hyperlink in hyperlinks:
            # Apply URL pattern filter
            if url_pattern and not re.search(url_pattern, hyperlink.url, re.IGNORECASE):
                continue
            
            # Apply text pattern filter
            if text_pattern and hyperlink.text and not re.search(text_pattern, hyperlink.text, re.IGNORECASE):
                continue
            
            filtered_links.append(hyperlink)
        
        return filtered_links

# Usage examples

# Extract only PDF links
pdf_links = extract_filtered_hyperlinks("document.html", url_pattern=r'\.pdf$')
print(f"Found {len(pdf_links)} PDF links")

# Extract links containing "download"
download_links = extract_filtered_hyperlinks("document.html", text_pattern=r'download')
print(f"Found {len(download_links)} download links")

# Extract external links (http/https)
external_links = extract_filtered_hyperlinks("document.html", url_pattern=r'^https?://')
print(f"Found {len(external_links)} external links")