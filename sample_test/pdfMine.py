from PyPDF2 import PdfReader, PdfWriter


def outline_textboxes(pdf_path, output_path):
  """Outlines text boxes in a PDF and saves the result to a new file."""
  reader = PdfReader(pdf_path)
  writer = PdfWriter()

  for page_num in range(len(reader.pages)):
    page = reader.pages[page_num]

    try:
      annotations = page['/Annots']
      # Rest of the code for processing annotations...
    except KeyError:
      print(f"Page {page_num + 1} does not contain any annotations to outline.")

  # ... rest of the code for writing the output PDF  

      for annotation in annotations:
            if annotation.get_subtype() == "/Widget":
                rect = annotation.get_rect()
                x1, y1, x2, y2 = rect

                outline_annotation = PdfWriter.PdfDictionary()
                outline_annotation.update(
                    {
                        "/Subtype": "/Annot",
                        "/Rect": [x1, y1, x2, y2],
                        "/AP": {"/N": {"/ linewidth": 2, "/C": [1, 0, 0]}},
                    }
                )
                page["/Annots"].append(outline_annotation)

      writer.addPage(page)

    with open(output_path, "wb") as output_file:
        writer.write(output_file)


# Example usage
pdf_path = "BEtest.pdf"
output_path = "updatedPDFs/outlineBEtest.pdf"
outline_textboxes(pdf_path, output_path)

print("Text boxes outlined in the new PDF: " + output_path)
