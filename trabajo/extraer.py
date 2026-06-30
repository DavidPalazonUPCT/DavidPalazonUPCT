import docx
from docx import Document
from docx.document import Document as DocType
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import Table
from docx.text.paragraph import Paragraph

doc = Document("insumos/Plan_Investigacion_v36_APA7.docx")

def iter_block_items(parent):
    if isinstance(parent, DocType):
        parent_elm = parent.element.body
    else:
        parent_elm = parent._tc
    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)

print("=== SECTIONS / PAGE SETUP ===")
for i, s in enumerate(doc.sections):
    print(f"section {i}: page {s.page_width} x {s.page_height}, margins L{s.left_margin} R{s.right_margin} T{s.top_margin} B{s.bottom_margin}")

print("\n=== STYLES IN USE ===")
from collections import Counter
style_counter = Counter()
for p in doc.paragraphs:
    style_counter[p.style.name] += 1
for name, count in style_counter.most_common():
    print(f"  {count:4d}  {name}")

print("\n=== BLOCK-BY-BLOCK (para idx | style | text preview) ===")
pidx = 0
for block in iter_block_items(doc):
    if isinstance(block, Paragraph):
        txt = block.text.strip()
        style = block.style.name
        # alignment
        algn = block.alignment
        preview = txt[:140].replace("\n"," ")
        print(f"[P{pidx:03d}] <{style}> {preview}")
        pidx += 1
    elif isinstance(block, Table):
        nrows = len(block.rows); ncols = len(block.columns)
        print(f"[TABLE] {nrows} rows x {ncols} cols")
        for r in block.rows:
            cells = [c.text.strip()[:40].replace('\n',' ') for c in r.cells]
            print("        | " + " | ".join(cells))
