from groupdocs.parser import Parser
from groupdocs.parser.data import Rectangle, Point, Size
from groupdocs.parser.templates import (
    Template,
    TemplateItem,
    TemplateTable,
    TemplateTableParameters,
)

table_area = Rectangle(Point(175.0, 350.0), Size(400.0, 200.0))
columns = [185.0, 370.0, 425.0, 485.0, 545.0]

table = TemplateTable(
    TemplateTableParameters(table_area, columns),
    "Details",
    0,  # restrict to the first page; omit to scan all pages
)

template = Template([table])

with Parser("./invoice.pdf") as parser:
    data = parser.parse_by_template(template)
    if data:
        details = data["Details"].page_area
        print(f"Rows extracted: {details.row_count}")