from groupdocs.parser import Parser

def process_large_table(file_path, max_rows_to_print=10):
    """
    Process large tables efficiently, showing only a preview.
    """
    with Parser(file_path) as parser:
        if not parser.features.tables:
            print("Table extraction not supported")
            return
        
        tables = parser.get_tables(None)
        
        if tables:
            for table_idx, table in enumerate(tables):
                print(f"\nTable {table_idx + 1}:")
                print(f"Total size: {table.row_count} rows × {table.column_count} columns")
                
                # Print header (first row)
                if table.row_count > 0:
                    print("\nHeader:")
                    for col in range(table.column_count):
                        cell = table[0, col]
                        if cell:
                            print(f"  Column {col + 1}: {cell.text}")
                
                # Print preview of data
                rows_to_show = min(max_rows_to_print, table.row_count)
                print(f"
Showing first {rows_to_show} rows:")
                
                for row in range(rows_to_show):
                    row_data = []
                    for col in range(table.column_count):
                        cell = table[row, col]
                        cell_text = cell.text[:20] if cell and cell.text else ""  # Truncate long text
                        row_data.append(cell_text)
                    print(" | ".join(row_data))

# Usage
process_large_table("large_spreadsheet.xlsx")