from groupdocs.parser import Parser
import xml.etree.ElementTree as ET

# Create an instance of Parser class
with Parser("./sample.docx") as parser:
    # Extract text structure
    xml_reader = parser.get_structure()
    
    # Check if structure extraction is supported
    if xml_reader is None:
        print("Text structure extraction isn't supported")
    else:
        # Read XML content
        xml_content = xml_reader
        print(xml_content)