from groupdocs.parser import Parser
from groupdocs.parser.options import SearchOptions

# Create an instance of Parser class
with Parser("./sample.docx") as parser:
    # Search for exact word match (case-insensitive, whole word)
    # Parameters: match_case=False, match_whole_word=True, use_regular_expression=False
    options = SearchOptions(False, True, False)
    
    search_results = parser.search("invoice", options)
    
    if search_results:
        print(f"Found {len(list(search_results))} occurrences of 'invoice' as whole word")