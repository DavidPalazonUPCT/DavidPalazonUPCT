"""Helpers para construir el cuerpo del .docx v37 reusando los estilos del v36.
Plantillas de formato capturadas del v36:
 - body Normal: spacing after=200 line=288 auto; ind firstLine=720; jc both; TNR 12pt (default)
 - Heading 1: pStyle Ttulo1; spacing line=288
 - Heading 2: pStyle Ttulo2; spacing line=288
 - Bibliografia: spacing after=100 line=288 auto; ind left=567 hanging=567; sz=20 (10pt)
 - Titulo portada: center; spacing after=500; bold; sz=36 (18pt)
 - Palabras clave: jc both; run1 bold+italic 'Palabras clave: ', run2 normal
"""
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from xml.sax.saxutils import escape

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'

def _p_from_xml(inner):
    from docx.oxml import parse_xml
    xml = f'<w:p xmlns:w="{W}">{inner}</w:p>'
    return parse_xml(xml)

def body_para(text, justify=True):
    jc = '<w:jc w:val="both"/>' if justify else ''
    inner = (f'<w:pPr><w:spacing w:after="200" w:line="288" w:lineRule="auto"/>'
             f'<w:ind w:firstLine="720"/>{jc}</w:pPr>'
             f'<w:r><w:t xml:space="preserve">{escape(text)}</w:t></w:r>')
    return _p_from_xml(inner)

def body_para_runs(runs):
    """runs: list of (text, bold, italic). One paragraph, justified, first-line indent."""
    rxml = ''
    for t, b, i in runs:
        rpr = ''
        if b or i:
            rpr = '<w:rPr>' + ('<w:b/>' if b else '') + ('<w:i/>' if i else '') + '</w:rPr>'
        rxml += f'<w:r>{rpr}<w:t xml:space="preserve">{escape(t)}</w:t></w:r>'
    inner = ('<w:pPr><w:spacing w:after="200" w:line="288" w:lineRule="auto"/>'
             '<w:ind w:firstLine="720"/><w:jc w:val="both"/></w:pPr>' + rxml)
    return _p_from_xml(inner)

def h1(text):
    inner = (f'<w:pPr><w:pStyle w:val="Ttulo1"/><w:spacing w:line="288" w:lineRule="auto"/></w:pPr>'
             f'<w:r><w:t xml:space="preserve">{escape(text)}</w:t></w:r>')
    return _p_from_xml(inner)

def h2(text):
    inner = (f'<w:pPr><w:pStyle w:val="Ttulo2"/><w:spacing w:line="288" w:lineRule="auto"/></w:pPr>'
             f'<w:r><w:t xml:space="preserve">{escape(text)}</w:t></w:r>')
    return _p_from_xml(inner)

def bib_para(text):
    inner = (f'<w:pPr><w:spacing w:after="100" w:line="288" w:lineRule="auto"/>'
             f'<w:ind w:left="567" w:hanging="567"/></w:pPr>'
             f'<w:r><w:rPr><w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr>'
             f'<w:t xml:space="preserve">{escape(text)}</w:t></w:r>')
    return _p_from_xml(inner)

def empty_para():
    return _p_from_xml('')
