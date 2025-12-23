from groupdocs.parser import Parser
from groupdocs.parser.options import PageTableAreaOptions
from groupdocs.parser.templates import TemplateTableLayout

# Create an instance of Parser class
with Parser("invoice.pdf") as parser:
    # Check if table extraction is supported
    if not parser.features.tables:
        print("Table extraction not supported")
        return
    
    # Define table layout (column and row separators in points)
    # Columns: x-coordinates of vertical separators
    # Rows: y-coordinates of horizontal separators
    layout = TemplateTableLayout(
        [50, 95, 275, 415, 485, 545],  # Column separators
        [325, 340, 365, 395]            # Row separators
    )
    
    # Create options for table extraction
    options = PageTableAreaOptions(layout)
    
    # Extract tables with custom layout
    tables = parser.get_tables(options)
    
    if tables:
        for table in tables:
            print(f"
Table: {table.row_count} rows × {table.column_count} columns")
            
            # Print table content
            for row in table.rows:
                for cell in row.cells:
                    if cell:
                        print(f"{cell.text} | ", end="")
                print()