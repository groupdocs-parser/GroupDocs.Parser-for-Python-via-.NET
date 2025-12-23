# GroupDocs.Parser for Python via .NET – Code Examples  

🚀 Welcome to the **GroupDocs.Parser for Python via .NET** repository!  

This repository contains runnable Python examples for **GroupDocs.Parser for Python via .NET**.

---  

## 📖 About GroupDocs.Parser for Python via .NET  

GroupDocs.Parser for Python via .NET is a powerful document‑parsing and data‑extraction library. It lets you extract **text, images, attachments, barcodes, and structured content** from a wide range of document formats, including PDF, Word, Excel, PowerPoint, emails, archives, e‑books and many image types. The library runs on **Windows, Linux and macOS** and works with any supported Python 3.5+ interpreter.  

---  

### Key Features  

- **Rich text extraction & search** – plain or formatted text, page‑level access, case‑sensitive, whole‑word and regex search.  
- **Structured content & templates** – parse headings, paragraphs, tables, text areas and use templates to pull strongly‑typed fields from invoices, receipts, etc.  
- **Images, attachments & barcodes** – extract embedded images, file attachments and barcodes from supported documents.  
- **OCR for scanned documents** – read text from scanned PDFs and raster images, with optional spell‑checking.  
- **Wide format & platform support** – dozens of document, image and archive formats on Windows, Linux and macOS, all via a unified .NET‑powered API accessed from Python.  

---  

### Supported Document Formats  

**Word Processing** – DOC, DOT, DOCX, DOCM, DOTX, DOTM, RTF, TXT, ODT, OTT  
**PDF** – PDF (full text, images, attachments, forms, barcode scanning)  
**Markup** – XHTML, MHTML, MD, XML  
**eBooks** – CHM, EPUB, FB2, MOBI, AZW3  
**Spreadsheets** – XLS, XLT, XLSX, XLSM, XLSB, XLTX, XLTM, ODS, OTS, CSV, XLA, XLAM, NUMBERS  
**Presentations** – PPT, PPS, POT, PPTX, PPTM, PPSX, PPSM, POTX, POTM, ODP, OTP  
**Email** – PST, OST, EML, EMLX, MSG  
**Notes** – ONE  
**Archives** – 7Z, ZIP, RAR, TAR, GZ, BZ2  
**Images** – BMP, GIF, JP2, JPG/JPEG, PNG, TIF/TIFF, DICOM, DJVU, EMF, J2K, PS, PSD, SVG, SVGZ, WEBP, WMF  

---  

### Getting Started  

#### Prerequisites  

- Python 3.5+  
- Windows, Linux or macOS with a supported Python runtime  

#### Installation  

```bash
pip install groupdocs-parser-net
```

Upgrade to the latest version:

```bash
pip install --upgrade groupdocs-parser-net
```

#### Quick Example – Extract Text from a PDF  

```python
from groupdocs.parser import Parser

with Parser("sample.pdf") as parser:
    text = parser.GetText()
    print(text)
```

#### Additional Small Samples  

**Search text in a PDF**

```python
from groupdocs.parser import Parser

with Parser("sample.pdf") as parser:
    for area in parser.Search("Total Amount"):
        print(f"Page {area.PageIndex}, Rectangle: {area.Rectangle}")
```

**Extract images from a Word document**

```python
from groupdocs.parser import Parser

with Parser("sample.docx") as parser:
    images = parser.GetImages()
    for i, image in enumerate(images, 1):
        image.Save(f"image{i}.png")
```

**Read document metadata**

```python
from groupdocs.parser import Parser

with Parser("sample.pdf") as parser:
    metadata = parser.GetMetadata()
    for item in metadata:
        print(f"{item.Name}: {item.Value}")
```

---  

## 📜 Licensing  

You can request a **30‑day Temporary License** for unrestricted testing:

1. Visit the **[Get a Temporary License](https://purchase.groupdocs.com/temp-license/114765/)** page.  
2. Follow the instructions to obtain the license file.  
3. Apply the license in your code:

```python
import os
from groupdocs.parser import License

license_path = os.path.abspath("./GroupDocs.Parser.lic")
License().set_license(license_path)
```

GroupDocs.Parser for Python via .NET is distributed under the GroupDocs End‑User License Agreement (EULA). For full pricing details see the **[pricing page](https://purchase.groupdocs.com/pricing/parser/python-net/)**.  

---  

## 🛠️ Support  

GroupDocs offers unlimited free technical support for all products, including evaluation versions.  

- **Free Support Forum** – Ask questions, share ideas and get help directly from the development team: <https://forum.groupdocs.com/c/parser>  
- **Paid Support Helpdesk** – Faster response times and dedicated assistance: <https://helpdesk.groupdocs.com/>  
- **Paid Consulting** – Custom development, feature requests or consulting services: <https://consulting.groupdocs.com/contact/>  

---  

## 📬 Stay Updated  

- 📘 Check other products: [GroupDocs Products Catalog](https://products.groupdocs.com/)  
- 💻 Download free trial: [GroupDocs Downloads](https://releases.groupdocs.com/)  
- 💬 Need help? Visit our [Free Support Forum](https://forum.groupdocs.com/).