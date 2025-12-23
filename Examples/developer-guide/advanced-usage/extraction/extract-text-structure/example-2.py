from groupdocs.parser import Parser
import xml.etree.ElementTree as ET

# Create an instance of Parser class
with Parser("sample.docx") as parser:
    # Extract text structure
    xml_reader = parser.get_structure()
    
    if xml_reader is None:
        print("Structure extraction not supported")
    else:
        # Parse XML
        xml_content = xml_reader
        root = ET.fromstring(xml_content)
        
        # Count elements
        sections = root.findall('.//section')
        paragraphs = root.findall('.//p')
        tables = root.findall('.//table')
        hyperlinks = root.findall('.//hyperlink')
        
        print(f"Document Structure Analysis:")
        print(f"  Sections: {len(sections)}")
        print(f"  Paragraphs: {len(paragraphs)}")
        print(f"  Tables: {len(tables)}")
        print(f"  Hyperlinks: {len(hyperlinks)}")