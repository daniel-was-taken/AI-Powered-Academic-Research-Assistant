import urllib.request

# Define the URL of the webpage containing the PDF
url = "http://arxiv.org/pdf/2402.04161v1"  # Replace with your actual URL

# Download the PDF
urllib.request.urlretrieve(url, "filename.pdf")

print(f"PDF downloaded successfully: filename.pdf")
