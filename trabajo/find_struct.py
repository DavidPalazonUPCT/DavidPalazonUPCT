from docx import Document
from docx.document import Document as DocType
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
import re
doc = Document("insumos/Plan_Investigacion_v36_APA7.docx")
# Find which paragraph index holds the embedded sectPr (section break = end of cover)
for i, p in enumerate(doc.paragraphs):
    if p._p.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pPr') is not None:
        ppr = p._p.pPr
        if ppr is not None and ppr.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}sectPr') is not None:
            print(f"Embedded sectPr found in paragraph index {i}: text={p.text[:40]!r}")
# Body order: list block items with index to locate the table position
body = doc.element.body
kids = list(body.iterchildren())
print(f"\nTotal direct children of body: {len(kids)}")
print("Last child tag:", kids[-1].tag.split('}')[-1])
# table info
tbls = doc.tables
print(f"\nTables: {len(tbls)}")
t = tbls[0]
print(f"Table 0: {len(t.rows)} rows x {len(t.columns)} cols")
# Dump grid + first column texts and shading of a couple cells
print("Row labels (col 0):")
for r in t.rows:
    print("  -", r.cells[0].text.strip()[:55])
