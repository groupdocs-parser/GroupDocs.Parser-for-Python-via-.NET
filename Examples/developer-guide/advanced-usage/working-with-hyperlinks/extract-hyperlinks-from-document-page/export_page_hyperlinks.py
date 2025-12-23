from groupdocs.parser import Parser
import json

def export_page_hyperlinks(file_path, output_json):
    """
    Extract hyperlinks by page and export to JSON.
    """
    with Parser(file_path) as parser:
        if not parser.features.hyperlinks:
            print("Hyperlink extraction not supported")
            return False
        
        info = parser.get_document_info()
        
        # Build structure
        document_links = {
            'file': file_path,
            'total_pages': info.page_count,
            'pages': []
        }
        
        for page_index in range(info.page_count):
            hyperlinks = parser.get_hyperlinks(page_index)
            
            page_data = {
                'page_number': page_index + 1,
                'hyperlinks': []
            }
            
            if hyperlinks:
                for link in hyperlinks:
                    page_data['hyperlinks'].append({
                        'text': link.text or '',
                        'url': link.url or ''
                    })
            
            document_links['pages'].append(page_data)
        
        # Save to JSON
        with open(output_json, 'w', encoding='utf-8') as f:
            json.dump(document_links, f, indent=2, ensure_ascii=False)
        
        print(f"Hyperlinks exported to {output_json}")
        return True

# Usage
export_page_hyperlinks("document.pdf", "hyperlinks_by_page.json")