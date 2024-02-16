from json import loads

template = '<table:table table:name="Table{table_number}" table:style-name="Table{table_number}"><table:table-column table:style-name="Table{table_number}.A"/><table:table-row table:style-name="TableLine94630472006064"><table:table-cell table:style-name="Table{table_number}.A1" office:value-type="string"><text:h text:style-name="P2" text:outline-level="1">{term}</text:h><text:p text:style-name="P4"/></table:table-cell></table:table-row><table:table-row table:style-name="TableLine94630472006064"><table:table-cell table:style-name="Table{table_number}.A1" office:value-type="string"><text:p text:style-name="P5">{definition}</text:p></table:table-cell></table:table-row></table:table><text:p text:style-name="P8"/>'

renderedTables = ""

with open("bookbinding-glossary.json", "r") as glossary_json:
    glossary = loads(glossary_json.read())
    counter = 1
    for record in glossary["bookbindingGlossary"]:
        print(record["term"])
        renderedTables += template.format(
                term=record["term"],
                definition=record["definition"],
                table_number=counter
        )

        counter += 1

    print(renderedTables)
