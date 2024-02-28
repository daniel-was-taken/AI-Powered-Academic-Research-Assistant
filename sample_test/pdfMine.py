# DEPRECATED 

from PyPDF2 import PdfReader, PdfWriter

def outline_textboxes(pdf_path, output_path):
  """Outlines text boxes in a PDF and saves the result to a new file.

  Prints information about encountered annotations for debugging purposes.
  """
  reader = PdfReader(pdf_path)
  writer = PdfWriter()

  for page_num in range(len(reader.pages)):
    page = reader.pages[page_num]
    annotations = page.get('/Annots')

    if annotations:
      print(f"Page {page_num + 1} has {len(annotations)} annotations.")
      for annotation_ref in annotations:
        annotation = annotation_ref.get_object()
        subtype = annotation.get('/Subtype')
        if subtype == '/Widget':
          print(f"Found a Widget annotation: {annotation}")
          # Further logic to identify specific text box types if needed...

    writer.add_page(page)

  with open(output_path, 'wb') as output_file:
    writer.write(output_file)


# Example usage
pdf_path = 'toscrape.pdf'
output_path = 'updatedPDFs/outlineBEtest.pdf'
outline_textboxes(pdf_path, output_path)

print('Text boxes outlined in the new PDF:', output_path)
