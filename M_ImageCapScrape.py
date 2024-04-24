import fitz  # PyMuPDF
from PyPDF2 import PdfReader 
import re

def extract_images_and_captions(pdf_path):
    pdf_document = fitz.open(pdf_path)
    images_with_captions = []
    images_cap = {}
    
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        images = page.get_images(full=True)
        page_text = pdf_document[page_num].get_text()

        # Use regex to find all captions associated with figures
        figure_captions = re.findall(r'\bFigure\s+\d+:\s+(.*)', page_text, re.IGNORECASE)
        # print(figure_captions)
        for img_index, img_info in enumerate(images):
            xref = img_info[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            
            if img_index < len(figure_captions):
                caption = figure_captions[img_index]
            else:
                caption = figure_captions[img_index-1]
            
            images_cap[caption] = image_bytes

            images_with_captions.append({
                "caption": caption,
                "image": image_bytes
            })
    
    pdf_document.close()
    return images_with_captions, images_cap

# Example usage
pdf_path = "./toscrape.pdf"
extracted_data , images_cap = extract_images_and_captions(pdf_path)

for k, v in images_cap.items():
    print(k, v)

# for entry in extracted_data:
#     caption = entry["caption"]
#     image_data = entry["image"]
    
    
    # Now you can save the image_data and caption to files or process them further
    # e.g., save image_data to an image file, and caption to a text file

 