from alexisomggeneratelatextable import generate_latex_table
from pdflatex import PDFLaTeX

latex = '''
\\documentclass{article}
\\begin{document}
'''
latex += generate_latex_table([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
latex += '\n\\end{document}'
pdfl = PDFLaTeX.from_binarystring(latex.encode('utf-8'), 'task2')
pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True)