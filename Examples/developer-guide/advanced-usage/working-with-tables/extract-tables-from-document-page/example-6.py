from groupdocs.parser import Parser
from groupdocs.parser.options import PageTableAreaOptions
from groupdocs.parser.templates import TemplateTableLayout

# Create an instance of Parser class
with Parser("invoice.pdf") as parser:
    if not parser.features.tables:
        print("Table extraction not supported")
        return
    
    # Define custom table layout
    layout = TemplateTableLayout(
        [50, 150, 300, 450],  # Column separators
        [200, 220, 240, 260]  # Row separators
    )
    
    # Create options for specific page with custom layout
    page_index = 0
    options = PageTableAreaOptions(page_index, layout)
    
    # Extract tables
    tables = parser.get_tables(options)
    
    if tables:
        print(f"Tables extracted from page {page_index + 1} with custom layout:")
        for table in tables:
            print(f"
Table: {table.row_count}×{table.column_count}")
            for row in range(table.row_count):
                for col in range(table.column_count):
                    cell = table[row, col]
                    if cell:
                        print(f"{cell.text:20}", end=" | ")
                print()