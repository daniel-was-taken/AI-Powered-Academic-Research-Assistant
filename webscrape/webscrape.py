# Go to https://arxiv.org/multi?group=grp_cs&%2Fform=Form+Interface

# In advanced search,
#     set Search terms = {Input from user(preprocessed)}
#     subject = computer science (CS)
#     EXTRA:  Date.

    # or

# use a preset query eg -announced_date_first; size: 50; include_cross_list: True; terms: AND title=Research on Quantum computing
# idk how the url will be 
# Download the first n(3) papers pdfs
#save PDFS in a temp folder (papers/paper1.. paper3)

import requests
import re
import csv
import pandas as pd
from bs4 import BeautifulSoup
keyword = input("Enter what you want to search for: ")
keyword = keyword.strip()
nkey = re.sub("\s", "+", keyword)
print(nkey)
test = "mobiles"
# url = f"https://www.flipkart.com/{test}/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi"
url = f"https://arxiv.org/search/?query={nkey}&searchtype=all&source=header"
r = requests.get(url)
print(r)


