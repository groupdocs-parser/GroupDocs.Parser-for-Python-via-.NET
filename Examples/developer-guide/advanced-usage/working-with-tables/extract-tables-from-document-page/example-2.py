from groupdocs.parser import Parser
from groupdocs.parser.options import PageTableAreaOptions

# Create an instance of Parser class
with Parser("./document.docx") as parser:
    # Check if table extraction is supported
    if not parser.features.tables:
        print("Table extraction not supported")
        return
    
    # Get document info
    info = parser.get_document_info()
    
    if info.page_count == 0:
        print("Document has no pages")
        return
    
    # Iterate over pages
    total_tables = 0
    for page_index in range(info.page_count):
        print(f"
{'=' * 50}")
        print(f"Page {page_index + 1}/{info.page_count}")
        print('=' * 50)
        
        # Create options for this page
        options = PageTableAreaOptions(page_index)
        
        # Extract tables from current page
        tables = parser.get_tables(options)
        
        if tables:
            page_table_count = 0
            for table in tables:
                page_table_count += 1
                total_tables += 1
                
                print(f"
Table {page_table_count}:")
                print(f"Size: {table.row_count}×{table.column_count}")
                print(f"Position: ({table.rectangle.left}, {table.rectangle.top})")
            
            print(f"
Tables on this page: {page_table_count}")
        else:
            print("No tables on this page")
    
    print(f"
{'=' * 50}")
    print(f"Total tables in document: {total_tables}")