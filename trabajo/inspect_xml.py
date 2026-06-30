from docx import Document
import re
doc = Document("insumos/Plan_Investigacion_v36_APA7.docx")
P = doc.paragraphs

def show(idx, label):
    p = P[idx]
    xml = p._p.xml
    # strip namespace noise for readability
    xml = re.sub(r' xmlns:[a-z0-9]+="[^"]*"', '', xml)
    print(f"\n===== P{idx:03d}  [{label}]  style={p.style.name!r}  text={p.text[:50]!r}")
    print(xml[:1600])

show(6, "TITULO portada")
show(9, "autor nombre")
show(35, "Heading 1")
show(58, "Heading 2")
show(36, "body Normal")
show(46, "lista numerada objetivo")
show(145, "bibliografia entrada 1")
show(40, "palabras clave")
