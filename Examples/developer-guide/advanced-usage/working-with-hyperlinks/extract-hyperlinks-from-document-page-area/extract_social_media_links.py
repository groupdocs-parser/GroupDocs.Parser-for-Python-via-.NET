from groupdocs.parser import Parser
from groupdocs.parser.options import PageAreaOptions, Rectangle, Point, Size

def extract_social_media_links(file_path, area_rect):
    """
    Extract social media links from a specific area.
    """
    x, y, w, h = area_rect
    area = Rectangle(Point(x, y), Size(w, h))
    options = PageAreaOptions(area)
    
    # Social media domains
    social_domains = [
        'facebook.com', 'twitter.com', 'linkedin.com',
        'instagram.com', 'youtube.com', 'tiktok.com'
    ]
    
    with Parser(file_path) as parser:
        if not parser.features.hyperlinks:
            print("Hyperlink extraction not supported")
            return {}
        
        hyperlinks = parser.get_hyperlinks(options)
        
        if not hyperlinks:
            return {}
        
        # Categorize by platform
        social_links = {}
        
        for link in hyperlinks:
            if link.url:
                for domain in social_domains:
                    if domain in link.url:
                        platform = domain.split('.')[0].capitalize()
                        if platform not in social_links:
                            social_links[platform] = []
                        social_links[platform].append(link.url)
                        break
        
        return social_links

# Usage - extract from footer area
footer_area = (0, 800, 600, 100)
social_links = extract_social_media_links("webpage.html", footer_area)

print("Social Media Links:")
for platform, urls in social_links.items():
    print(f"  {platform}: {', '.join(urls)}")