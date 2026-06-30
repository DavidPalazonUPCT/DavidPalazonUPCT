# -*- coding: utf-8 -*-
"""FASE 4: genera Plan_Investigacion_v37.docx partiendo del v36 (preserva estilos)."""
import re, copy
from docx import Document
from docx.oxml import parse_xml
from docx.oxml.ns import qn
from xml.sax.saxutils import escape

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
def P(inner): return parse_xml(f'<w:p xmlns:w="{W}">{inner}</w:p>')

def parse_inline(text):
    """-> list of (text, bold, italic). Handles **bold** and *italic* (no nesting)."""
    runs=[]; pos=0
    for m in re.finditer(r'\*\*(.+?)\*\*|\*(.+?)\*', text):
        if m.start()>pos: runs.append((text[pos:m.start()],False,False))
        if m.group(1) is not None: runs.append((m.group(1),True,False))
        else: runs.append((m.group(2),False,True))
        pos=m.end()
    if pos<len(text): runs.append((text[pos:],False,False))
    return runs or [(text,False,False)]

def runs_xml(runs, base_rpr=''):
    out=''
    for t,b,i in runs:
        rpr=''
        props = (('<w:b/>' if b else '')+('<w:i/>' if i else ''))
        if props or base_rpr: rpr='<w:rPr>'+base_rpr+props+'</w:rPr>'
        out+=f'<w:r>{rpr}<w:t xml:space="preserve">{escape(t)}</w:t></w:r>'
    return out

def body_para(text):
    inner=('<w:pPr><w:spacing w:after="200" w:line="288" w:lineRule="auto"/>'
           '<w:ind w:firstLine="720"/><w:jc w:val="both"/></w:pPr>'+runs_xml(parse_inline(text)))
    return P(inner)

def keywords_para(rest):
    r=('<w:r><w:rPr><w:b/><w:i/></w:rPr><w:t xml:space="preserve">Palabras clave: </w:t></w:r>'
       +runs_xml(parse_inline(rest)))
    return P('<w:pPr><w:spacing w:after="200" w:line="288" w:lineRule="auto"/><w:jc w:val="both"/></w:pPr>'+r)

def h1(text):
    return P(f'<w:pPr><w:pStyle w:val="Ttulo1"/><w:spacing w:line="288" w:lineRule="auto"/></w:pPr>'+runs_xml(parse_inline(text)))
def h2(text):
    return P(f'<w:pPr><w:pStyle w:val="Ttulo2"/><w:spacing w:line="288" w:lineRule="auto"/></w:pPr>'+runs_xml(parse_inline(text)))

def toc_para(text, level):
    base = '<w:rPr><w:b/></w:rPr>' if level==0 else ''
    ind = '<w:ind w:left="440"/>' if level==1 else ''
    r = (f'<w:r>{base}<w:t xml:space="preserve">{escape(text)}</w:t></w:r>')
    return P(f'<w:pPr><w:spacing w:after="80" w:line="288" w:lineRule="auto"/>{ind}</w:pPr>'+r)

def bib_para(text):
    inner=('<w:pPr><w:spacing w:after="100" w:line="288" w:lineRule="auto"/>'
           '<w:ind w:left="567" w:hanging="567"/></w:pPr>'
           +runs_xml(parse_inline(text), base_rpr='<w:sz w:val="20"/><w:szCs w:val="20"/>'))
    return P(inner)

def cell(text, w, fill=None, bold=False, sz=None, jc=None):
    bd=''.join(f'<w:{s} w:val="single" w:sz="2" w:space="0" w:color="888888"/>' for s in ('top','left','bottom','right'))
    shd=f'<w:shd w:val="clear" w:color="auto" w:fill="{fill}"/>' if fill else ''
    rpr=('<w:rPr>'+('<w:b/>' if bold else '')+(f'<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/>' if sz else '')+'</w:rPr>') if (bold or sz) else ''
    runs = runs_xml(parse_inline(text), base_rpr=(f'<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/>' if sz else '')+('<w:b/>' if bold else ''))
    jcx=f'<w:jc w:val="{jc}"/>' if jc else ''
    ppr=f'<w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/>{jcx}</w:pPr>'
    return (f'<w:tc><w:tcPr><w:tcW w:w="{w}" w:type="dxa"/><w:tcBorders>{bd}</w:tcBorders>{shd}'
            f'<w:vAlign w:val="center"/></w:tcPr>{P(ppr+runs).xml if False else f"<w:p>{ppr}{runs}</w:p>"}</w:tc>')

def build_positioning_table(rows):
    # rows: list of [c1,c2,c3]; first row header. 3 cols.
    widths=[2600,3000,3400]
    trs=''
    for ri,row in enumerate(rows):
        hdr = ri==0
        cells=''.join(cell(row[c], widths[c], fill=('D9E2F3' if hdr else None), bold=hdr, sz='18') for c in range(3))
        trs+=f'<w:tr>{cells}</w:tr>'
    return parse_xml(f'<w:tbl xmlns:w="{W}"><w:tblPr><w:tblW w:w="9000" w:type="dxa"/>'
                     f'<w:tblBorders>'+''.join(f'<w:{s} w:val="single" w:sz="2" w:space="0" w:color="888888"/>' for s in ('top','left','bottom','right','insideH','insideV'))+
                     f'</w:tblBorders><w:tblLook w:val="04A0"/></w:tblPr>'
                     f'<w:tblGrid>'+''.join(f'<w:gridCol w:w="{w}"/>' for w in widths)+f'</w:tblGrid>{trs}</w:tbl>')

# ---------- parse plan_v37.md ----------
md = open('trabajo/plan_v37.md').read()
# title
title = re.search(r'## TÍTULO.*?\n\n\*\*(.+?)\*\*', md, re.S).group(1).strip()
# body from "## 1." onward
body_md = md[md.index('## 1. Resumen'):]
body_part, bib_part = body_md.split('## 7. Bibliografía')

blocks=[]; i=0
lines=body_part.split('\n')
while i < len(lines):
    ln=lines[i].rstrip()
    if not ln.strip() or ln.strip()=='---': i+=1; continue
    if ln.startswith('## '):
        blocks.append(('h1', ln[3:].strip()))
    elif ln.startswith('### '):
        blocks.append(('h2', ln[4:].strip()))
    elif ln.startswith('**Palabras clave:**'):
        blocks.append(('kw', ln.replace('**Palabras clave:**','').strip()))
    elif ln.strip()=='[TABLA_CRONOGRAMA]':
        blocks.append(('cron',))
    elif ln.lstrip().startswith('|'):
        tbl=[]
        while i<len(lines) and lines[i].lstrip().startswith('|'):
            cells=[c.strip() for c in lines[i].strip().strip('|').split('|')]
            if not re.match(r'^[-\s|]+$', lines[i].strip().strip('|')): tbl.append(cells)
            i+=1
        blocks.append(('postable', tbl)); continue
    elif re.match(r'^- \*\*', ln) or re.match(r'^\d+\.\s', ln):
        blocks.append(('body', re.sub(r'^- ','',ln).strip()))
    else:
        blocks.append(('body', ln.strip()))
    i+=1

# TOC structure (regenerated)
toc=[("1. Resumen del proyecto de tesis",0),
("2. Objetivos científicos e hipótesis",0),("2.1. Objetivos",1),("2.2. Hipótesis",1),
("3. Introducción y estado del tema",0),("3.1. Justificación",1),
("3.2. Infraestructuras hídricas críticas y su ciberseguridad",1),
("3.3. Técnicas de inteligencia artificial para la detección de anomalías en series OT",1),
("3.4. Detección fiable y evaluación realista de despliegue",1),
("3.5. Deriva, contexto operativo y robustez",1),
("3.6. La explicabilidad como consecuencia de la detección",1),
("3.7. Estructuración del contexto y transferibilidad",1),
("4. Metodología y plan de trabajo",0),("4.1. Marco metodológico",1),
("4.2. Diseño experimental y panel de evaluación",1),
("4.3. Organización del trabajo: paquetes de trabajo e hilo teórico",1),
("4.4. Cronograma y duración prevista",1),
("4.5. Instalaciones, instrumentos y técnicas disponibles",1),
("5. Posicionamiento frente al estado del arte",0),
("6. Interés científico y aplicabilidad",0),
("7. Bibliografía",0)]

# ---------- cronograma: clone v36 table, relabel + reshade ----------
doc = Document("insumos/Plan_Investigacion_v36_APA7.docx")
cron = copy.deepcopy(doc.tables[0]._tbl)
# new task labels (rows 2..11) and gantt fills (cols 1..16), 1-indexed quarter
TASKS=[("Corriente A: Revisión sistemática continua de la literatura", list(range(1,17)), '4472C4'),
("Corriente B: Infraestructura experimental reproducible", list(range(1,17)), '4472C4'),
("WP0: Marco conceptual (fundamentos, dominio y datos)", [1,2,3,4], '4472C4'),
("WP1: Diagnóstico teórico — revisión acotada (Paper 1)", [3,4,5,6], '4472C4'),
("WP2: Diagnóstico empírico — caracterización (Paper 2)", [5,6,7,8,9,10], '4472C4'),
("WP3: Propuesta — detector régimen-condicionado (Paper 3)", [7,8,9,10,11,12,13], '4472C4'),
("Hilo teórico: transferibilidad y contexto operativo", [6,7,8,9,10,11,12,13,14], 'D9E2F3'),
("Viabilidad de despliegue (comprobación operativa)", [9,10,11,12], 'D9E2F3'),
("Redacción y difusión", list(range(5,17)), '4472C4'),
("Integración y memoria final", [13,14,15,16], '4472C4')]
rows = cron.findall(qn('w:tr'))
for r_i, (label, fills, color) in enumerate(TASKS):
    tr = rows[2+r_i]
    tcs = tr.findall(qn('w:tc'))
    # label cell 0: replace text
    c0 = tcs[0]
    for t in c0.iter(qn('w:t')): t.text=''
    # set first run text
    ts = c0.findall('.//'+qn('w:t'))
    if ts: ts[0].text = label
    # gantt cells 1..16
    for q in range(1,17):
        if q>=len(tcs): break
        tc = tcs[q]
        tcPr = tc.find(qn('w:tcPr'))
        # remove existing shd
        for shd in tcPr.findall(qn('w:shd')): tcPr.remove(shd)
        if q in fills:
            shd = parse_xml(f'<w:shd xmlns:w="{W}" w:val="clear" w:color="auto" w:fill="{color}"/>')
            tcPr.append(shd)

# ---------- assemble document ----------
body = doc.element.body
sectPr = body.findall(qn('w:sectPr'))[-1]
# update title text (P006)
paras = doc.paragraphs
for p in paras[:15]:
    if 'Contribuciones a la detección' in p.text:
        for r in p.runs[1:]: r.text=''
        p.runs[0].text = title
        break
# remove from P015 (TOC heading 'Índice') to before final sectPr
cover_end = paras[14]._p
removing=False
to_rm=[]
for ch in list(body.iterchildren()):
    if ch is cover_end: removing=True; continue
    if removing:
        if ch is sectPr: break
        to_rm.append(ch)
for ch in to_rm: body.remove(ch)

def ins(el): sectPr.addprevious(el)
# TOC
ins(h1("Índice de contenidos"))
for txt,lvl in toc: ins(toc_para(txt,lvl))
ins(P(''))  # blank
# body blocks
for blk in blocks:
    k=blk[0]
    if k=='h1': ins(h1(blk[1]))
    elif k=='h2': ins(h2(blk[1]))
    elif k=='kw': ins(keywords_para(blk[1]))
    elif k=='body': ins(body_para(blk[1]))
    elif k=='cron':
        ins(copy.deepcopy(cron))
    elif k=='postable':
        ins(build_positioning_table(blk[1]))
# bibliography
ins(h1("7. Bibliografía"))
for line in bib_part.split('\n'):
    s=line.strip()
    if not s or s=='---': continue
    s=re.sub(r'\s*\[VERIFICAR MANUALMENTE[^\]]*\]','',s).strip()
    ins(bib_para(s))

doc.save("Plan_Investigacion_v37.docx")
print("Saved Plan_Investigacion_v37.docx")
# validate
d2=Document("Plan_Investigacion_v37.docx")
print("Reload OK. Paragraphs:", len(d2.paragraphs), "Tables:", len(d2.tables))
