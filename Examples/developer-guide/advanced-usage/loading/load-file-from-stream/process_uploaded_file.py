from groupdocs.parser import Parser
from io import BytesIO

def process_uploaded_file(file_content, filename):
    """Process an uploaded file without saving it to disk"""
    
    try:
        # Create a stream from the file content
        stream = BytesIO(file_content)
        
        # Create parser instance
        with Parser(stream) as parser:
            print(f"Processing uploaded file: {filename}")
            
            # Get document info
            doc_info = parser.get_document_info()
            print(f"File type: {doc_info.file_type.file_format}")
            print(f"Pages: {doc_info.page_count}")
            
            # Extract text
            text_reader = parser.get_text()
            if text_reader:
                text = text_reader
                
                return {
                    "success": True,
                    "filename": filename,
                    "type": doc_info.file_type.file_format,
                    "pages": doc_info.page_count,
                    "text_length": len(text),
                    "text": text
                }
            else:
                return {
                    "success": False,
                    "error": "Text extraction not supported"
                }
                
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

# Example: Simulate uploaded file
with open("sample.docx", "rb") as f:
    file_content = f.read()

result = process_uploaded_file(file_content, "sample.docx")
print(result)