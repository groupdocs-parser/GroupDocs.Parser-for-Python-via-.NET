from groupdocs.parser import Parser
from groupdocs.parser.options import PageTableAreaOptions

def compare_tables_across_pages(file_path, page_indices):
    """
    Compare table structures across multiple pages.
    """
    with Parser(file_path) as parser:
        if not parser.features.tables:
            print("Table extraction not supported")
            return
        
        page_table_info = {}
        
        for page_index in page_indices:
            options = PageTableAreaOptions(page_index)
            tables = parser.get_tables(options)
            
            if tables:
                table_list = list(tables)
                page_table_info[page_index + 1] = {
                    'count': len(table_list),
                    'structures': [(t.row_count, t.column_count) for t in table_list]
                }
            else:
                page_table_info[page_index + 1] = {
                    'count': 0,
                    'structures': []
                }
        
        # Print comparison
        print("Table Structure Comparison:")
        print(f"{'Page':<10}{'Tables':<10}{'Structures':<40}")
        print("-" * 60)
        
        for page_num, info in sorted(page_table_info.items()):
            structures_str = ", ".join([f"{r}×{c}" for r, c in info['structures']])
            print(f"{page_num:<10}{info['count']:<10}{structures_str:<40}")

# Usage
compare_tables_across_pages("financial_report.pdf", [0, 1, 2, 3, 4])