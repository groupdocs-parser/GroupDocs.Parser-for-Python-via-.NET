from groupdocs.parser import Parser
from groupdocs.parser.options import PageTableAreaOptions

# Create an instance of Parser class
with Parser("./report.pdf") as parser:
    # Check if table extraction is supported
    if not parser.features.tables:
        print("Table extraction not supported")
        return
    
    # Create options for page-specific extraction
    page_index = 0  # First page
    options = PageTableAreaOptions(page_index)
    
    # Extract tables from the specified page
    tables = parser.get_tables(options)
    
    if tables:
        print(f"Tables on page {page_index + 1}:")
        for table_idx, table in enumerate(tables):
            print(f"
Table {table_idx + 1}:")
            print(f"Size: {table.row_count} rows × {table.column_count} columns")
            
            # Print table content
            for row in range(table.row_count):
                row_data = []
                for col in range(table.column_count):
                    cell = table[row, col]
                    cell_text = cell.text if cell else ""
                    row_data.append(cell_text)
                print(" | ".join(row_data))
    else:
        print(f"No tables found on page {page_index + 1}")