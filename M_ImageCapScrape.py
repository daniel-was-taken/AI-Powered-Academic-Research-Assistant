import fitz  # PyMuPDF
from PyPDF2 import PdfReader 
import re
import PIL.Image
from PIL import Image
import io
import base64

def extract_images_and_captions(pdf_path):
    print(pdf_path)

    pdf_document = fitz.open(pdf_path)
    images_with_captions = []
    images_cap = {}
    
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        images = page.get_images(full=True)
        page_text = pdf_document[page_num].get_text()

        # Use regex to find all captions associated with figures
        # figure_captions = re.findall(r'\bFigure\s+\d+.*\d*:\s+(.*)', page_text, re.IGNORECASE)
        figure_captions = [match.group() for match in re.finditer(r'\bFig\b.*\d+.+',page_text)]
        # print(figure_captions)
        for img_index, img_info in enumerate(images):
            xref = img_info[0]
            base_image = pdf_document.extract_image(xref)
            # extension = base_image["ext"]
            # img = PIL.Image.open(io.BytesIO(base_image["image"]))
            # img.save(open(f"OCR_Rec/Images/Captions/{xref}.{extension}", "wb"))
            image_bytes = base_image["image"]
            
            if img_index < len(figure_captions):
                caption = figure_captions[img_index]
            else:
                try:
                    caption = figure_captions[img_index-1]
                except:
                    caption = None
            pil_image = Image.open(io.BytesIO(image_bytes))
            buffered = io.BytesIO()
            pil_image.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            


            images_cap[caption] = img_str
            # images_cap[caption] = image_bytes


            # pil_image = Image.open(io.BytesIO(image_bytes))

            images_with_captions.append({
                "caption": caption,
                "image": image_bytes
            })

        # page_text = re.sub(r'\n+', '\n', page_text)  # Normalize newlines
        # page_text = re.sub(r'\n\s+', '\n', page_text)  # Remove leading spaces after newlines
        # page_text = re.sub(r'\s+\n', '\n', page_text)  # Remove trailing spaces before newlines
        # page_text = re.sub(r'\s+', ' ', page_text)  # Replace multiple spaces with a single space


        # output_file = 'OCR_Rec/Text/' + "imageCap" + '.txt'
        # with open(output_file, 'a', encoding='utf-8') as file:
        #     file.write(page_text)

        # figure_captions = [match.group() for match in re.finditer(r'\b(Fig).*\d+.+',page_text)]
    
    pdf_document.close()
    # return images_with_captions, images_cap
    return images_cap


# Example usage
pdf_path = "./OnlyPDFs/MyReport2.pdf"

# extracted_data , images_cap = extract_images_and_captions(pdf_path)
images_cap = extract_images_and_captions(pdf_path)

for k, v in images_cap.items():
    print(k)