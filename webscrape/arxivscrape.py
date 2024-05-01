#pip install arxiv
import pandas as pd
import arxiv

def scrape(topic):
  # topic = input("Enter the topic you need to search for : ")
  # num = int(input("Enter how many papers you want: "))
  client = arxiv.Client()
  # Refined Topic based on CS
  refined_topic = f"cat:cs* AND ti:{topic}"
  print(refined_topic)
  num = 3
  search = arxiv.Search(
    query = f"cat:cs* AND ti:{topic}",
    # query = refined_topic,
    max_results = num,
    sort_by = arxiv.SortCriterion.SubmittedDate,
    # sort_order = arxiv.SortOrder.Descending
  )

  for r in client.results(search):
    print(r.title)

  all_data = []
  for result in search.results():
    temp = ["","","","",""]
    temp[0] = result.title
    temp[1] = result.published
    temp[2] = result.entry_id
    temp[3] = result.summary
    temp[4] = result.pdf_url
    all_data.append(temp)

  column_names = ['Title','Date','Id','Summary','URL']
  df = pd.DataFrame(all_data, columns=column_names)

  print("Number of papers extracted : ",df.shape[0])
  
  print(df.head())
  data = {"Title":df["Title"],"ID":df["Id"],"URL": df['URL'],"Summary":df['Summary']}
  df1 = pd.DataFrame(data)
  data2 = {"URL":df["URL"]}
  df2 = pd.DataFrame(data2)
  df2.to_csv("OnlyURL.csv",index=False)
  df1.to_csv("Scrape.csv", index=False)

