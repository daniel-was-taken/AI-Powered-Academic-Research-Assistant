import fitz
import PIL.Image
import io
import pdfminer

pdf = fitz.open("toscrape.pdf")
counter = 1


for i in range(len(pdf)):
    page = pdf[i]
    images = page.get_images()
    for image in images:
        base_img = pdf.extract_image(image[0])

# The code originally saves the image flipped 
# vertically and horizontally hence we the below code

        # Flip the image 180 degrees
        img = PIL.Image.open(io.BytesIO(base_img["image"])).rotate(180)
        img = img.transpose(PIL.Image.FLIP_LEFT_RIGHT)
        #
        extension = base_img["ext"]
        img.save(open(f"images/image{counter}.{extension}", "wb"))
        counter += 1