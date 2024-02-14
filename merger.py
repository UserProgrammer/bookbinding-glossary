import linecache
from json import dumps

with open("terms", "r") as terms_file, open("definitions") as definitions_file:
    bookbinding_glossary = {"bookbindingGlossary": []}

    for line_number in range(1, 170):
        term = terms_file.readline().replace("\n", "")
        if (term == ""):
            break
        definition = definitions_file.readline().replace("\n", "")
        bookbinding_glossary["bookbindingGlossary"].append({
            "term": term,
            "definition": definition
        })

    print(dumps(bookbinding_glossary))
