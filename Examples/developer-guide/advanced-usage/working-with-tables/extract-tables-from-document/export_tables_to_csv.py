from groupdocs.parser import Parser
import csv
import os

def export_tables_to_csv(file_path, output_dir):
    """
    Extract tables from document and save as CSV files.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    with Parser(file_path) as parser:
        if not parser.features.tables:
            print("Table extraction not supported")
            return
        
        tables = parser.get_tables(None)
        
        if not tables:
            print("No tables found")
            return
        
        for table_idx, table in enumerate(tables):
            # Create CSV filename
            csv_filename = f"table_{table_idx + 1}.csv"
            csv_path = os.path.join(output_dir, csv_filename)
            
            # Write table to CSV
            with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                
                # Write table rows
                for row in table.rows:
                    row_data = []
                    for cell in row.cells:
                        cell_text = cell.text if cell else ""
                        row_data.append(cell_text)
                    writer.writerow(row_data)
            
            print(f"Saved: {csv_path}")

# Usage
export_tables_to_csv("report.xlsx", "exported_tables")