from groupdocs.parser import Parser
from groupdocs.parser.options import SearchOptions, HighlightOptions

def advanced_search(file_path, pattern, case_sensitive=False, use_regex=False):
    """
    Perform advanced text search with highlights and page numbers.
    """
    try:
        with Parser(file_path) as parser:
            # Configure highlight options
            highlight_opts = HighlightOptions(20)
            
            # Configure search options
            search_opts = SearchOptions(
                match_case=case_sensitive,
                match_whole_word=False,
                use_regular_expression=use_regex,
                search_by_pages=True,
                left_highlight_options=highlight_opts,
                right_highlight_options=highlight_opts
            )
            
            # Perform search
            results = parser.search(pattern, search_opts)
            
            if results is None:
                print("Search not supported for this document")
                return []
            
            # Process results
            found_items = []
            for result in results:
                found_items.append({
                    'text': result.text,
                    'position': result.position,
                    'page': result.page_index + 1,
                    'left_context': result.left_highlight_item.text if result.left_highlight_item else "",
                    'right_context': result.right_highlight_item.text if result.right_highlight_item else ""
                })
            
            return found_items
            
    except Exception as e:
        print(f"Error during search: {e}")
        return []

# Usage
results = advanced_search("sample.pdf", r"\d{4}-\d{2}-\d{2}", use_regex=True)
for item in results:
    print(f"Page {item['page']}: {item['left_context']}[{item['text']}]{item['right_context']}")