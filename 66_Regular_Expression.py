import re

pattern = r"[A-Z]+ll"

text = '''The main use of News All API is to search through every article published by over 80,000 news sources and blogs in the last 5 years. Think of us as Google News that you can interact with programmatically!
In this example we want to find all  articles that mention DOll Apple published today, and sort them by most popular source first (i.e. Engadget articles will be returned ahead of Mom and Pop's Little iPhone Blog). For this we need to use the /everything endpoint.'''

#match = re.search(pattern,text)
match = re.finditer(pattern,text)

for matches in match:
    print(matches)