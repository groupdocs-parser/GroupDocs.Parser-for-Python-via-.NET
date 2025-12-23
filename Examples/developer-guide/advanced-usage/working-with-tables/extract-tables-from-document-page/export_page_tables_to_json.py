from groupdocs.parser import Parser
from groupdocs.parser.options import PageTableAreaOptions
import json

def export_page_tables_to_json(file_path, page_index, output_file):
    """
    Export tables from a specific page to JSON format.
    """
    with Parser(file_path) as parser:
        if not parser.features.tables:
            print("Table extraction not supported")
            return
        
        options = PageTableAreaOptions(page_index)
        tables = parser.get_tables(options)
        
        if not tables:
            print(f"No tables found on page {page_index + 1}")
            return
        
        # Build JSON structure
        page_data = {
            'page_number': page_index + 1,
            'tables': []
        }
        
        for table_idx, table in enumerate(tables):
            table_data = {
                'table_index': table_idx + 1,
                'rows': table.row_count,
                'columns': table.column_count,
                'data': []
            }
            
            # Extract table data
            for row in range(table.row_count):
                row_data = []
                for col in range(table.column_count):
                    cell = table[row, col]
                    row_data.append(cell.text if cell else "")
                table_data['data'].append(row_data)
            
            page_data['tables'].append(table_data)
        
        # Save to JSON
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(page_data, f, indent=2, ensure_ascii=False)
        
        print(f"Exported {len(page_data['tables'])} tables from page {page_index + 1} to {output_file}")

# Usage
export_page_tables_to_json("data.pdf", 0, "page1_tables.json")