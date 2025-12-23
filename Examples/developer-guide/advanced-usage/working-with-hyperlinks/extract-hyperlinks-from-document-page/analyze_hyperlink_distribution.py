from groupdocs.parser import Parser
from collections import defaultdict

def analyze_hyperlink_distribution(file_path):
    """
    Analyze how hyperlinks are distributed across pages.
    """
    with Parser(file_path) as parser:
        if not parser.features.hyperlinks:
            print("Hyperlink extraction not supported")
            return
        
        info = parser.get_document_info()
        
        # Collect statistics
        stats = []
        domain_frequency = defaultdict(int)
        
        for page_index in range(info.page_count):
            hyperlinks = parser.get_hyperlinks(page_index)
            
            if hyperlinks:
                link_list = list(hyperlinks)
                page_stat = {
                    'page': page_index + 1,
                    'count': len(link_list),
                    'unique_urls': len(set(link.url for link in link_list))
                }
                stats.append(page_stat)
                
                # Count domains
                for link in link_list:
                    if link.url:
                        try:
                            from urllib.parse import urlparse
                            domain = urlparse(link.url).netloc or "internal"
                            domain_frequency[domain] += 1
                        except:
                            pass
        
        # Print analysis
        print(f"Hyperlink Distribution Analysis:")
        print(f"{'Page':<10}{'Links':<10}{'Unique URLs':<15}")
        print("-" * 35)
        
        for stat in stats:
            print(f"{stat['page']:<10}{stat['count']:<10}{stat['unique_urls']:<15}")
        
        print(f"
Top domains:")
        for domain, count in sorted(domain_frequency.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"  {domain}: {count}")

# Usage
analyze_hyperlink_distribution("documentation.pdf")