from groupdocs.parser import Parser

# Create an instance of Parser class
with Parser("report.pdf") as parser:
    if not parser.features.tables:
        print("Table extraction not supported")
        return
    
    # Get document info
    info = parser.get_document_info()
    print(f"Document has {info.page_count} pages")
    
    # Extract all tables
    tables = parser.get_tables(None)
    
    if tables:
        # Group tables by page
        tables_by_page = {}
        for table in tables:
            page_num = table.page.index + 1
            if page_num not in tables_by_page:
                tables_by_page[page_num] = []
            tables_by_page[page_num].append(table)
        
        # Print summary
        print(f"
Found {len(list(tables))} tables across {len(tables_by_page)} pages")
        
        for page_num in sorted(tables_by_page.keys()):
            page_tables = tables_by_page[page_num]
            print(f"
Page {page_num}: {len(page_tables)} table(s)")
            
            for idx, table in enumerate(page_tables):
                print(f"  Table {idx + 1}: {table.row_count}×{table.column_count}")