from groupdocs.parser import Parser
from groupdocs.parser.templates import Template, TemplateField, TemplateRegexPosition

template = Template([
    TemplateField(
        TemplateRegexPosition(r"Invoice Number\s+(?<value>[A-Z0-9\-]+)"),
        "InvoiceNumber",
    )
])

with Parser("./invoice.pdf") as parser:
    data = parser.parse_by_template(template)
    if data:
        invoice_number = data["InvoiceNumber"].page_area.text
        print(f"Invoice number: {invoice_number}")