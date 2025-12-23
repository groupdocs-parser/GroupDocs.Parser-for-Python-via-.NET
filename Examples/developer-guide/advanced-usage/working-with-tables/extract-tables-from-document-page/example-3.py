from groupdocs.parser import Parser
from groupdocs.parser.options import PageTableAreaOptions

# Create an instance of Parser class
with Parser("report.xlsx") as parser:
    if not parser.features.tables:
        print("Table extraction not supported")
        return
    
    # Define pages to process (e.g., pages 1, 3, and 5)
    pages_to_process = [0, 2, 4]  # Zero-based indices
    
    for page_index in pages_to_process:
        print(f"
Processing page {page_index + 1}...")
        
        # Create options for this page
        options = PageTableAreaOptions(page_index)
        
        # Extract tables from this page
        tables = parser.get_tables(options)
        
        if tables:
            for table_idx, table in enumerate(tables):
                print(f"  Table {table_idx + 1}: {table.row_count}×{table.column_count}")
                
                # Show first row as sample
                if table.row_count > 0:
                    print("  First row:", end=" ")
                    for col in range(min(3, table.column_count)):  # Show first 3 columns
                        cell = table[0, col]
                        if cell:
                            print(f"[{cell.text}]", end=" ")
                    print("...")
        else:
            print(f"  No tables found on page {page_index + 1}")