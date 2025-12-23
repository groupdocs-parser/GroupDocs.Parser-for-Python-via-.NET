from groupdocs.parser import Parser
from groupdocs.parser.options import SearchOptions

# Create an instance of Parser class
with Parser("./sample.pdf") as parser:
    # Create search options with page search enabled
    # Parameters: match_case, match_whole_word, use_regular_expression, search_by_pages
    options = SearchOptions(False, False, False, True)
    
    # Search with page numbers
    search_results = parser.search("lorem", options)
    
    if search_results is None:
        print("Search isn't supported")
    else:
        # Iterate over search results
        for result in search_results:
            # Print position, page number, and found text
            print(f"At {result.position} (page {result.page_index + 1}): {result.text}")