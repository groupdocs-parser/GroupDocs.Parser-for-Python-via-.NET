from groupdocs.parser import Parser
import csv

def export_inventory_to_csv(file_path, output_csv):
    """
    Export container inventory to CSV file.
    """
    with Parser(file_path) as parser:
        attachments = parser.get_container()
        
        if attachments is None:
            print("Container extraction not supported")
            return False
        
        # Write to CSV
        with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Index', 'Name', 'Size (bytes)', 'Path']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            
            for idx, attachment in enumerate(attachments, 1):
                writer.writerow({
                    'Index': idx,
                    'Name': attachment.name,
                    'Size (bytes)': attachment.size,
                    'Path': attachment.file_path or ''
                })
        
        print(f"Inventory exported to {output_csv}")
        return True

# Usage
export_inventory_to_csv("archive.zip", "inventory.csv")