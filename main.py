import os
from sys import argv

from docx import Document
from ukrainian_word_stress import Stressifier, StressSymbol

filename = argv[1]
suffix = "_nagolos"
name, ext = os.path.splitext(filename)
new_filename = name + suffix + ext

source = Document(filename)
out = Document()
stressify = Stressifier(stress_symbol=StressSymbol.CombiningAcuteAccent)

for paragraph in source.paragraphs:
    out.add_paragraph(stressify(paragraph.text))

out.save(new_filename)
