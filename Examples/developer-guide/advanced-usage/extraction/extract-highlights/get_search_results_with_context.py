from groupdocs.parser import Parser
from groupdocs.parser.options import SearchOptions, HighlightOptions

def get_search_results_with_context(file_path, keyword, context_length=30):
    """
    Search for keyword and extract surrounding context.
    """
    with Parser(file_path) as parser:
        # Create highlight options for context
        highlight_opts = HighlightOptions(context_length)
        
        # Create search options with highlights
        search_opts = SearchOptions(
            match_case=False,
            match_whole_word=False,
            use_regular_expression=False,
            left_highlight_options=highlight_opts,
            right_highlight_options=highlight_opts
        )
        
        # Search for keyword
        results = parser.search(keyword, search_opts)
        
        if results is None:
            print("Search not supported")
            return []
        
        # Collect results with context
        search_results = []
        for result in results:
            left_context = result.left_highlight_item.text if result.left_highlight_item else ""
            right_context = result.right_highlight_item.text if result.right_highlight_item else ""
            
            search_results.append({
                'keyword': result.text,
                'position': result.position,
                'page': result.page_index + 1 if hasattr(result, 'page_index') else None,
                'left_context': left_context,
                'right_context': right_context,
                'full_snippet': f"{left_context}[{result.text}]{right_context}"
            })
        
        return search_results

# Usage
results = get_search_results_with_context("sample.pdf", "artificial intelligence", 40)

print(f"Found {len(results)} occurrences:
")
for idx, result in enumerate(results, 1):
    print(f"{idx}. {result['full_snippet']}")
    if result['page']:
        print(f"   (Page {result['page']}, position {result['position']})
")