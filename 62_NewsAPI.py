import requests
import json

query = input("what type of news are you interested in ?")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-05-05&sortBy=publishedAt&apiKey=8b56439cc2664a55aceea5a5518a34bc"

r =requests.get(url)
news = json.loads(r.text)

#print(r.text)


for artical in news["articles"]:
    print(artical["title"])
    print(artical["description"])
    print("-----------------------------------")
