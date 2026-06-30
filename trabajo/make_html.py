# -*- coding: utf-8 -*-
import re, html
md=open('trabajo/plan_v37.md').read()
title=re.search(r'## TÍTULO.*?\n\n\*\*(.+?)\*\*', md, re.S).group(1).strip()
body_md=md[md.index('## 1. Resumen'):]

def inl(t):
    t=html.escape(t)
    t=re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t=re.sub(r'\*(.+?)\*', r'<i>\1</i>', t)
    return t

# cronograma data (mirror del docx)
TASKS=[("Corriente A: Revisión sistemática continua",list(range(1,17)),'d'),
("Corriente B: Infraestructura experimental reproducible",list(range(1,17)),'d'),
("WP0: Marco conceptual (fundamentos, dominio y datos)",[1,2,3,4],'d'),
("WP1: Diagnóstico teórico — revisión acotada (Paper 1)",[3,4,5,6],'d'),
("WP2: Diagnóstico empírico — caracterización (Paper 2)",[5,6,7,8,9,10],'d'),
("WP3: Propuesta — detector régimen-condicionado (Paper 3)",[7,8,9,10,11,12,13],'d'),
("Hilo teórico: transferibilidad y contexto operativo",[6,7,8,9,10,11,12,13,14],'l'),
("Viabilidad de despliegue (comprobación operativa)",[9,10,11,12],'l'),
("Redacción y difusión",list(range(5,17)),'d'),
("Integración y memoria final",[13,14,15,16],'d')]
def cron_html():
    h='<table class="gantt"><tr><th rowspan=2>TAREAS</th>'+''.join(f'<th colspan=4>AÑO {y}</th>' for y in range(1,5))+'</tr><tr>'+('<th>Q1</th><th>Q2</th><th>Q3</th><th>Q4</th>'*4)+'</tr>'
    for lab,fills,col in TASKS:
        cells=''.join(f'<td class="{ ("dk" if col=="d" else "lt") if q in fills else "" }"></td>' for q in range(1,17))
        h+=f'<tr><td class="lab">{html.escape(lab)}</td>{cells}</tr>'
    return h+'</table>'

out=[]
out.append(f'<div class="cover"><div class="esc">ESCUELA INTERNACIONAL DE DOCTORADO</div><div class="prog">Programa de Doctorado Tecnologías de la Computación e Ingeniería Ambiental</div><h1 class="tit">{html.escape(title)}</h1><div class="aut">Autor:<br>David Palazón Palau</div><div class="dir">Directores:<br>Dr. D. Juan Miguel Navarro Ruiz<br>Dr. D. Antonio Pita Lozano</div><div class="city">Murcia, Junio de 2026</div></div>')

body_part,bib_part=body_md.split('## 7. Bibliografía')
lines=body_part.split('\n'); i=0
while i<len(lines):
    ln=lines[i].rstrip()
    if not ln.strip() or ln.strip()=='---': i+=1; continue
    if ln.startswith('## '): out.append(f'<h2sec>{inl(ln[3:])}</h2sec>'.replace('h2sec','h1'))
    elif ln.startswith('### '): out.append(f'<h2>{inl(ln[4:])}</h2>')
    elif ln.startswith('**Palabras clave:**'): out.append(f'<p class="kw"><b><i>Palabras clave:</i></b> {inl(ln.replace("**Palabras clave:**","").strip())}</p>')
    elif ln.strip()=='[TABLA_CRONOGRAMA]': out.append(cron_html())
    elif ln.lstrip().startswith('|'):
        rows=[]
        while i<len(lines) and lines[i].lstrip().startswith('|'):
            cs=[c.strip() for c in lines[i].strip().strip('|').split('|')]
            if not re.match(r'^[-\s|]+$', lines[i].strip().strip('|')): rows.append(cs)
            i+=1
        th='<table class="pos"><tr>'+''.join(f'<th>{inl(c)}</th>' for c in rows[0])+'</tr>'
        for r in rows[1:]: th+='<tr>'+''.join(f'<td>{inl(c)}</td>' for c in r)+'</tr>'
        out.append(th+'</table>'); continue
    elif re.match(r'^- ', ln): out.append(f'<p class="bul">{inl(ln[2:])}</p>')
    else: out.append(f'<p>{inl(ln.strip())}</p>')
    i+=1
out.append('<h1>7. Bibliografía</h1>')
for l in bib_part.split('\n'):
    s=l.strip()
    if not s or s=='---': continue
    s=re.sub(r'\s*\[VERIFICAR MANUALMENTE[^\]]*\]','',s).strip()
    out.append(f'<p class="bib">{inl(s)}</p>')

css="""@page{size:A4;margin:2.54cm}body{font-family:'Times New Roman',serif;font-size:12pt;line-height:1.4;text-align:justify}
h1{font-size:14pt;font-weight:bold;margin:14pt 0 6pt;page-break-after:avoid}h2{font-size:12.5pt;font-weight:bold;margin:10pt 0 4pt;page-break-after:avoid}
p{margin:0 0 6pt;text-indent:1.25cm}p.kw,p.bul{text-indent:0}p.bib{font-size:10pt;text-indent:0;padding-left:1cm;text-indent:-1cm;margin-bottom:3pt}
.cover{text-align:center;page-break-after:always;padding-top:1cm}.cover .esc{font-size:13pt;font-weight:bold;margin-top:1cm}.cover .prog{font-size:12pt;margin:6pt 0 3cm}
.cover .tit{font-size:18pt;font-weight:bold;line-height:1.3;margin:0 1cm 3cm}.cover .aut,.cover .dir{font-size:14pt;margin:10pt 0}.cover .city{font-size:14pt;margin-top:3cm}
table{border-collapse:collapse;width:100%;font-size:9pt;margin:6pt 0;page-break-inside:avoid}
table.pos{font-size:9pt}table.pos th,table.pos td{border:1px solid #888;padding:3px;text-align:left;vertical-align:top}table.pos th{background:#D9E2F3}
table.gantt th,table.gantt td{border:1px solid #888;text-align:center;font-size:8pt;height:14px}table.gantt td.lab{text-align:left;width:26%;padding:2px 4px}
table.gantt td.dk{background:#4472C4}table.gantt td.lt{background:#D9E2F3}"""
open('trabajo/plan_v37.html','w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{"".join(out)}</body></html>')
print("HTML escrito")
