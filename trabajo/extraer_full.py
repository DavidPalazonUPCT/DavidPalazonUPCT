import docx, json
from docx import Document
from docx.document import Document as DocType
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import Table
from docx.text.paragraph import Paragraph

doc = Document("insumos/Plan_Investigacion_v36_APA7.docx")

def iter_block_items(parent):
    parent_elm = parent.element.body if isinstance(parent, DocType) else parent._tc
    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)

lines = []
meta = []
pidx = 0
for block in iter_block_items(doc):
    if isinstance(block, Paragraph):
        txt = block.text
        style = block.style.name
        pf = block.paragraph_format
        # capture hanging indent
        hang = None
        try:
            if pf.first_line_indent is not None:
                hang = pf.first_line_indent.pt
        except: pass
        runs_info = [(r.text, bool(r.bold), bool(r.italic)) for r in block.runs]
        meta.append({"idx": pidx, "style": style, "text": txt, "hang": hang,
                     "align": str(block.alignment), "runs": len(block.runs)})
        if style.startswith("Heading 1"):
            lines.append(f"\n# [P{pidx:03d}] {txt}\n")
        elif style.startswith("Heading 2"):
            lines.append(f"\n## [P{pidx:03d}] {txt}\n")
        else:
            lines.append(f"[P{pidx:03d}] {txt}")
        pidx += 1
    elif isinstance(block, Table):
        lines.append("\n[TABLA]")
        for r in block.rows:
            cells = [c.text.strip().replace('\n',' ') for c in r.cells]
            lines.append("| " + " | ".join(cells) + " |")
        lines.append("")

with open("trabajo/plan_actual.md", "w") as f:
    f.write("\n".join(lines))
with open("trabajo/plan_actual_meta.json", "w") as f:
    json.dump(meta, f, ensure_ascii=False, indent=1)

print(f"Total paragraphs: {pidx}")
NL=chr(10); print("plan_actual.md written:", len(NL.join(lines)), "chars")
# count bibliography entries (after Bibliografía heading)
