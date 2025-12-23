from groupdocs.parser import Parser

def extract_text_safely(file_path):
    try:
        with Parser(file_path) as parser:
            # Check feature support
            if not parser.features.text:
                print(f"Text extraction not supported for {file_path}")
                return None
            
            # Extract text
            text_reader = parser.get_text()
            if text_reader is not None:
                return text_reader
            
    except Exception as e:
        print(f"Error extracting text: {e}")
        return None

# Usage
text = extract_text_safely("sample.docx")
if text:
    print(f"Extracted {len(text)} characters")