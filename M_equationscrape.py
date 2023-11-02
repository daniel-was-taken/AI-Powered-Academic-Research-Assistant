from pdfreader import SimplePDFViewer, PageDoesNotExist

fd = open("BEtest.pdf", "rb")
viewer = SimplePDFViewer(fd)

plain_text = ""
pdf_markdown = ""
images = []
try:
    while True:
        viewer.render()
        pdf_markdown += viewer.canvas.text_content
        plain_text += "".join(viewer.canvas.strings)
        images.extend(viewer.canvas.inline_images)
        images.extend(viewer.canvas.images.values())
        viewer.next()
except PageDoesNotExist:
    pass


output_file = 'text/textscrape.txt'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(plain_text)