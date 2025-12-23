from groupdocs.parser import Parser

# Excel file path
excel_path = "data.xlsx"

# Create an instance of Parser class
with Parser(excel_path) as parser:
    # Check if table extraction is supported
    if not parser.features.tables:
        print("Table extraction not supported for this file")
        return
    
    # Extract tables (pass None for automatic detection)
    tables = parser.get_tables(None)
    
    if tables:
        for table_idx, table in enumerate(tables):
            print(f"
Table {table_idx + 1}:")
            print(f"Size: {table.row_count} rows × {table.column_count} columns")
            print(f"Page: {table.page.index + 1}")
            
            # Print table data
            for row in table.rows:
                row_data = []
                for cell in row.cells:
                    cell_text = cell.text if cell else ""
                    row_data.append(cell_text)
                print(" | ".join(row_data))