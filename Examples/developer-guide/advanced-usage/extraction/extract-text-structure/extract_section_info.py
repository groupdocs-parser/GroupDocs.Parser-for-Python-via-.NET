from groupdocs.parser import Parser
import xml.etree.ElementTree as ET

def extract_section_info(file_path):
    """
    Extract section information from document.
    """
    with Parser(file_path) as parser:
        xml_reader = parser.get_structure()
        
        if xml_reader is None:
            print("Structure extraction not supported")
            return
        
        # Parse XML
        xml_content = xml_reader
        root = ET.fromstring(xml_content)
        
        # Find all sections
        sections = root.findall('.//section')
        
        print(f"Document has {len(sections)} sections:
")
        
        for idx, section in enumerate(sections, 1):
            name = section.get('name', f'Section {idx}')
            style = section.get('style', 'default')
            
            # Count elements in section
            paragraphs = section.findall('.//p')
            tables = section.findall('.//table')
            lists = section.findall('.//ul') + section.findall('.//ol')
            
            print(f"Section: {name}")
            print(f"  Style: {style}")
            print(f"  Paragraphs: {len(paragraphs)}")
            print(f"  Tables: {len(tables)}")
            print(f"  Lists: {len(lists)}")
            print()

# Usage
extract_section_info("sample.pptx")