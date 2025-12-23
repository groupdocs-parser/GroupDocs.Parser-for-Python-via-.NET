from groupdocs.parser import Parser
import csv

def export_hyperlinks_to_csv(file_path, output_csv):
    """
    Extract hyperlinks and save to CSV file.
    """
    with Parser(file_path) as parser:
        if not parser.features.hyperlinks:
            print("Hyperlink extraction not supported")
            return False
        
        hyperlinks = parser.get_hyperlinks()
        
        if not hyperlinks:
            print("No hyperlinks found")
            return False
        
        # Write to CSV
        with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Text', 'URL', 'Page', 'X', 'Y', 'Width', 'Height']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            
            for hyperlink in hyperlinks:
                writer.writerow({
                    'Text': hyperlink.text or '',
                    'URL': hyperlink.url or '',
                    'Page': hyperlink.page.index + 1,
                    'X': hyperlink.rectangle.left,
                    'Y': hyperlink.rectangle.top,
                    'Width': hyperlink.rectangle.width,
                    'Height': hyperlink.rectangle.height
                })
        
        print(f"Hyperlinks exported to {output_csv}")
        return True

# Usage
export_hyperlinks_to_csv("document.pdf", "hyperlinks.csv")