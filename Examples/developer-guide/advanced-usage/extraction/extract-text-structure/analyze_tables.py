from groupdocs.parser import Parser
import xml.etree.ElementTree as ET

def analyze_tables(file_path):
    """
    Analyze table structure in document.
    """
    with Parser(file_path) as parser:
        xml_reader = parser.get_structure()
        
        if xml_reader is None:
            print("Structure extraction not supported")
            return
        
        # Parse XML
        xml_content = xml_reader
        root = ET.fromstring(xml_content)
        
        # Find all tables
        tables = root.findall('.//table')
        
        print(f"Found {len(tables)} tables:
")
        
        for idx, table in enumerate(tables, 1):
            rows = table.findall('.//tr')
            
            print(f"Table {idx}:")
            print(f"  Rows: {len(rows)}")
            
            # Get column count from first row
            if rows:
                cells = rows[0].findall('.//td')
                print(f"  Columns: {len(cells)}")
            
            # Show cell spanning
            cells_with_span = table.findall('.//td[@rowSpan]') + table.findall('.//td[@columnSpan]')
            if cells_with_span:
                print(f"  Cells with spanning: {len(cells_with_span)}")
            
            print()

# Usage
analyze_tables("sample.xlsx")