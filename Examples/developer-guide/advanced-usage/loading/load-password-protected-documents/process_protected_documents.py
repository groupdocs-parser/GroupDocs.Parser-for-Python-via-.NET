from groupdocs.parser import Parser
from groupdocs.parser.options import LoadOptions
import os

def process_protected_documents(directory, password):
    """Process all password-protected documents in a directory"""
    
    results = []
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if not os.path.isfile(file_path):
            continue
        
        try:
            print(f"
Processing: {filename}")
            
            # Create LoadOptions with password
            load_options = LoadOptions(password)
            
            # Try to parse the document
            with Parser(file_path, load_options) as parser:
                # Get document info
                doc_info = parser.get_document_info()
                
                # Extract text
                text_reader = parser.get_text()
                text = text_reader if text_reader else ""
                
                results.append({
                    "filename": filename,
                    "type": doc_info.file_type.file_format,
                    "pages": doc_info.page_count,
                    "text_length": len(text),
                    "success": True
                })
                
                print(f"  ✓ Success - {len(text)} characters extracted")
                
        except Exception as e:
            print(f"  ✗ Failed - {e}")
            results.append({
                "filename": filename,
                "success": False,
                "error": str(e)
            })
    
    return results

# Process all protected documents
results = process_protected_documents("./protected_docs", "common-password")

# Print summary
successful = [r for r in results if r.get("success")]
print(f"
{len(successful)}/{len(results)} documents processed successfully")