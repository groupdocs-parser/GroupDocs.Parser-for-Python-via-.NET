from groupdocs.parser import Parser
import xml.etree.ElementTree as ET

def extract_formatted_text(file_path):
    """
    Extract text with formatting (bold, italic).
    """
    with Parser(file_path) as parser:
        xml_reader = parser.get_structure()
        
        if xml_reader is None:
            print("Structure extraction not supported")
            return
        
        # Parse XML
        xml_content = xml_reader
        root = ET.fromstring(xml_content)
        
        # Find formatted text
        bold_texts = root.findall('.//strong')
        italic_texts = root.findall('.//em')
        
        print("Bold text:")
        for text in bold_texts:
            if text.text:
                print(f"  - {text.text}")
        
        print("\nItalic text:")
        for text in italic_texts:
            if text.text:
                print(f"  - {text.text}")

# Usage
extract_formatted_text("sample.docx")