from groupdocs.parser import Parser

def save_structure_to_file(file_path, output_xml):
    """
    Extract and save document structure to XML file.
    """
    with Parser(file_path) as parser:
        xml_reader = parser.get_structure()
        
        if xml_reader is None:
            print("Structure extraction not supported")
            return False
        
        # Read and save XML
        xml_content = xml_reader
        
        with open(output_xml, 'w', encoding='utf-8') as f:
            f.write(xml_content)
        
        print(f"Structure saved to {output_xml}")
        return True

# Usage
save_structure_to_file("sample.pdf", "structure.xml")