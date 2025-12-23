from groupdocs.parser import Parser
from groupdocs.parser.options import SearchOptions

# Create an instance of Parser class
with Parser("./sample.pdf") as parser:
    # Create search options for regex search
    # Parameters: match_case, match_whole_word, use_regular_expression
    options = SearchOptions(True, False, True)
    
    # Search with a regular expression (case-sensitive)
    search_results = parser.search(r"page number: \d+", options)
    
    # Check if search is supported
    if search_results is None:
        print("Search isn't supported")
    else:
        # Iterate over search results
        for result in search_results:
            print(f"At {result.position}: {result.text}")