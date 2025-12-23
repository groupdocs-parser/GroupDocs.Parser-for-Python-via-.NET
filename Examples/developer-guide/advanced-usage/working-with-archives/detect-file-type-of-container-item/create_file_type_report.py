from groupdocs.parser import Parser
import json

def create_file_type_report(file_path, output_json):
    """
    Create detailed file type report for container contents.
    """
    with Parser(file_path) as parser:
        attachments = parser.get_container()
        
        if attachments is None:
            print("Container extraction not supported")
            return False
        
        report = {
            'container': file_path,
            'items': [],
            'summary': {}
        }
        
        type_counts = {}
        
        for attachment in attachments:
            item_info = {
                'name': attachment.name,
                'size': attachment.size,
                'path': attachment.file_path or ''
            }
            
            try:
                with attachment.open_parser() as file_parser:
                    info = file_parser.get_document_info()
                    
                    if info and info.file_type:
                        file_type = info.file_type.file_format
                        extension = info.file_type.extension
                        
                        item_info['file_type'] = file_type
                        item_info['extension'] = extension
                        item_info['page_count'] = info.page_count if hasattr(info, 'page_count') else None
                        
                        # Update counts
                        type_counts[file_type] = type_counts.get(file_type, 0) + 1
                    else:
                        item_info['file_type'] = 'Unknown'
                        type_counts['Unknown'] = type_counts.get('Unknown', 0) + 1
            
            except Exception as e:
                item_info['file_type'] = 'Error'
                item_info['error'] = str(e)
                type_counts['Error'] = type_counts.get('Error', 0) + 1
            
            report['items'].append(item_info)
        
        report['summary'] = {
            'total_items': len(report['items']),
            'type_distribution': type_counts
        }
        
        # Save report
        with open(output_json, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"File type report saved to {output_json}")
        print(f"
Summary:")
        print(f"  Total items: {report['summary']['total_items']}")
        for file_type, count in sorted(type_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"  {file_type}: {count}")
        
        return True

# Usage
create_file_type_report("archive.zip", "file_type_report.json")