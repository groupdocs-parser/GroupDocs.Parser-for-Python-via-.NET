from groupdocs.parser import Parser
from groupdocs.parser.options import SearchOptions, HighlightOptions

# Create an instance of Parser class
with Parser("./sample.pdf") as parser:
    # Create highlight options (extract 15 characters around the match)
    highlight_options = HighlightOptions(15)
    
    # Create search options with highlights
    search_options = SearchOptions(
        match_case=False,
        match_whole_word=False,
        use_regular_expression=False,
        left_highlight_options=highlight_options,
        right_highlight_options=highlight_options
    )
    
    # Search with highlights
    search_results = parser.search("lorem", search_options)
    
    if search_results is None:
        print("Search isn't supported")
    else:
        # Iterate over search results and print with highlights
        for result in search_results:
            left_text = result.left_highlight_item.text if result.left_highlight_item else ""
            right_text = result.right_highlight_item.text if result.right_highlight_item else ""
            print(f"{left_text}[{result.text}]{right_text}")