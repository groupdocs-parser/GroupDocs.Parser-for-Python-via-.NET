from groupdocs.parser import Parser
import xml.etree.ElementTree as ET

def extract_hyperlinks_from_structure(file_path):
    """
    Extract all hyperlinks using document structure.
    """
    with Parser(file_path) as parser:
        xml_reader = parser.get_structure()
        
        if xml_reader is None:
            print("Structure extraction not supported")
            return []
        
        # Parse XML
        xml_content = xml_reader
        root = ET.fromstring(xml_content)
        
        # Find all hyperlink elements
        hyperlinks = []
        for hyperlink in root.findall('.//hyperlink'):
            url = hyperlink.get('link', '')
            text = hyperlink.text or ''
            
            if url:
                hyperlinks.append({
                    'text': text,
                    'url': url
                })
        
        return hyperlinks

# Usage
links = extract_hyperlinks_from_structure("sample.pdf")
print(f"Found {len(links)} hyperlinks:
")
for link in links:
    print(f"  {link['text']} -> {link['url']}")