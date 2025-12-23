from groupdocs.parser import Parser

# Create an instance of Parser class
with Parser("./sample.xlsx") as parser:
    # Check if table extraction is supported
    if not parser.features.tables:
        print("Table extraction isn't supported")
        return
    
    # Extract tables from the document
    tables = parser.get_tables(None)
    
    if tables:
        table_index = 0
        for table in tables:
            table_index += 1
            print(f"
=== Table {table_index} ===")
            print(f"Rows: {table.row_count}, Columns: {table.column_count}")
            
            # Iterate over rows
            for row_index in range(table.row_count):
                # Iterate over columns
                for col_index in range(table.column_count):
                    # Get table cell
                    cell = table[row_index, col_index]
                    if cell:
                        print(f"{cell.text}\t", end="")
                print()  # New line after each row