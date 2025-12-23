from groupdocs.parser import Parser
from groupdocs.parser.options import TextOptions
import time

def compare_extraction_modes(file_path):
    """
    Compare performance between Accurate and Raw modes.
    """
    # Accurate mode
    start_time = time.time()
    with Parser(file_path) as parser:
        text_reader = parser.get_text()
        if text_reader:
            accurate_text = text_reader
            accurate_time = time.time() - start_time
            accurate_length = len(accurate_text)
        else:
            print("Text extraction not supported")
            return
    
    # Raw mode
    start_time = time.time()
    with Parser(file_path) as parser:
        options = TextOptions(False)
        text_reader = parser.get_text(options)
        if text_reader:
            raw_text = text_reader
            raw_time = time.time() - start_time
            raw_length = len(raw_text)
    
    # Print comparison
    print(f"Performance Comparison:")
    print(f"{'Mode':<15} {'Time (s)':<15} {'Length':<15} {'Speed':<15}")
    print("-" * 60)
    print(f"{'Accurate':<15} {accurate_time:<15.3f} {accurate_length:<15} {'1.0x':<15}")
    print(f"{'Raw':<15} {raw_time:<15.3f} {raw_length:<15} {accurate_time/raw_time:.2f}x faster")

# Usage
compare_extraction_modes("sample.pdf")