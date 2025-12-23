from groupdocs.parser import Parser

# Create an instance of Parser class
with Parser("./sample.pdf") as parser:
    # Search for a keyword
    search_results = parser.search("invoice")
    
    # Check if search is supported
    if search_results is None:
        print("Search isn't supported")
    else:
        # Iterate over search results
        for result in search_results:
            # Print position and found text
            print(f"At {result.position}: {result.text}")