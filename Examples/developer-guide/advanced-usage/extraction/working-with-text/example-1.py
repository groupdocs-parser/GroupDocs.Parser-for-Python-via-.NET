from groupdocs.parser import Parser

with Parser("sample.pdf") as parser:
    results = parser.search("GroupDocs")
    if results is None:
        print("Search isn't supported for this format.")
    else:
        for result in results:
            print(f"Found on page {result.page.index + 1}: {result.text}")