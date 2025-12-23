from groupdocs.parser import Parser

# Create an instance of Parser class
with Parser("document.docx") as parser:
    if not parser.features.tables:
        print("Table extraction not supported")
        return
    
    tables = parser.get_tables(None)
    
    if tables:
        for table in tables:
            print(f"
Table: {table.row_count}×{table.column_count}")
            print(f"Position: {table.rectangle}")
            
            # Access specific cell
            if table.row_count > 0 and table.column_count > 0:
                cell = table[0, 0]  # First cell
                if cell:
                    print(f"
First cell:")
                    print(f"  Text: {cell.text}")
                    print(f"  Row index: {cell.row_index}")
                    print(f"  Column index: {cell.column_index}")
                    print(f"  Row span: {cell.row_span}")
                    print(f"  Column span: {cell.column_span}")