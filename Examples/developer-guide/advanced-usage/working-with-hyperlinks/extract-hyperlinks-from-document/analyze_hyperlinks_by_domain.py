from groupdocs.parser import Parser
from urllib.parse import urlparse
from collections import defaultdict

def analyze_hyperlinks_by_domain(file_path):
    """
    Group hyperlinks by domain and show statistics.
    """
    with Parser(file_path) as parser:
        if not parser.features.hyperlinks:
            print("Hyperlink extraction not supported")
            return
        
        hyperlinks = parser.get_hyperlinks()
        
        if not hyperlinks:
            print("No hyperlinks found")
            return
        
        # Group by domain
        by_domain = defaultdict(list)
        
        for hyperlink in hyperlinks:
            try:
                parsed_url = urlparse(hyperlink.url)
                domain = parsed_url.netloc or "internal"
                by_domain[domain].append(hyperlink)
            except:
                by_domain["invalid"].append(hyperlink)
        
        # Print statistics
        print(f"Total hyperlinks: {sum(len(links) for links in by_domain.values())}")
        print(f"Unique domains: {len(by_domain)}
")
        
        # Sort by count
        sorted_domains = sorted(by_domain.items(), key=lambda x: len(x[1]), reverse=True)
        
        print(f"{'Domain':<40} {'Count':<10}")
        print("-" * 50)
        for domain, links in sorted_domains[:20]:  # Top 20
            print(f"{domain:<40} {len(links):<10}")

# Usage
analyze_hyperlinks_by_domain("article.html")