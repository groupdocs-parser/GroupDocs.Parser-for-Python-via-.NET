from groupdocs.parser import Parser
import re

def is_valid_url(url):
    """
    Basic URL validation.
    """
    url_pattern = re.compile(
        r'^(https?|ftp)://'  # Protocol
        r'([a-zA-Z0-9.-]+)'   # Domain
        r'(:[0-9]+)?'         # Optional port
        r'(/.*)?$'            # Optional path
    )
    return url_pattern.match(url) is not None

# Create an instance of Parser class
with Parser("webpage.html") as parser:
    if not parser.features.hyperlinks:
        print("Hyperlink extraction not supported")
        return
    
    # Extract hyperlinks
    hyperlinks = parser.get_hyperlinks()
    
    if hyperlinks:
        valid_links = []
        invalid_links = []
        
        for hyperlink in hyperlinks:
            if is_valid_url(hyperlink.url):
                valid_links.append(hyperlink)
            else:
                invalid_links.append(hyperlink)
        
        print(f"Valid hyperlinks: {len(valid_links)}")
        print(f"Invalid hyperlinks: {len(invalid_links)}")
        
        print("\nValid URLs:")
        for link in valid_links[:10]:  # Show first 10
            print(f"  {link.text} -> {link.url}")