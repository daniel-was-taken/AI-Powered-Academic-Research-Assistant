import csv
import requests
import os

def download_all_pdfs(csv_file, base_filename="Pdf", target_folder="ScrapedPDFs"):

  os.makedirs(target_folder, exist_ok=True)

  with open(csv_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row 
    for i, row in enumerate(reader):
      pdf_url = row[0]
      filename = f"{base_filename}{i + 1}.pdf"

      full_path = os.path.join(target_folder, filename)

      response = requests.get(pdf_url, stream=True)

      if response.status_code == 200:
        with open(full_path, "wb") as f:
          for chunk in response.iter_content(1024):
            if chunk:
              f.write(chunk)
          print(f"Downloaded PDF: {full_path}")
      else:
        print(f"Failed to download PDF from {pdf_url}")

csv_file = "OnlyURL.csv"
base_filename = "MyReport"
target_folder = "OnlyPDFs"

download_all_pdfs(csv_file, base_filename, target_folder)
