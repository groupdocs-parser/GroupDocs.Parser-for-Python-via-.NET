from groupdocs.parser import Parser
from groupdocs.parser.templates import Template, TemplateField, TemplateFixedPosition
from groupdocs.parser.data import Rectangle, Point, Size

template = Template([
    TemplateField(
        TemplateFixedPosition(Rectangle(Point(35.0, 135.0), Size(100.0, 10.0))),
        "CompanyName",
    ),
    TemplateField(
        TemplateFixedPosition(Rectangle(Point(35.0, 150.0), Size(100.0, 10.0))),
        "InvoiceNumber",
    ),
])

with Parser("./invoice.pdf") as parser:
    data = parser.parse_by_template(template)
    if data is None:
        print("Parsing by template isn't supported for this format.")
    else:
        # DocumentData exposes extracted fields as an indexed collection.
        for i in range(data.count):
            field = data[i]
            area = field.page_area
            text = getattr(area, "text", None)
            print(f"{field.name}: {text if text is not None else '[non-text value]'}")