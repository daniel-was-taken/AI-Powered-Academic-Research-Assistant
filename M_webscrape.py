from pdfreader import SimplePDFViewer, PageDoesNotExist

fd = open("BEtest.pdf", "rb")
viewer = SimplePDFViewer(fd)

plain_text = ""

try:
    while True:
        viewer.render()
        plain_text += "".join(viewer.canvas.strings)
        viewer.next()
except PageDoesNotExist:
    pass


output_file = 'text/textscrape.txt'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(plain_text)