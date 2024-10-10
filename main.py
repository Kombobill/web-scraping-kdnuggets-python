from bs4 import BeautifulSoup
import requests

url = "https://www.kdnuggets.com/"
res = requests.get(url)
htmlData = res.content
# print(htmlData)

# //to this point, we extract raw html content.Text , paragraphs,anchortags,divs..all ..next task is to parse data for text and tags separately//
# //un comment print(htmlData)..to validate the above step..

parsedData = BeautifulSoup(htmlData, "html.parser")
# print(parsedData.prettify())

# Parse html

soup = BeautifulSoup("<h1> Welcome to KDnuggets! </h1>", "html.parser")
# print(type(soup))....to this step...we covert the html to beatifulsoup for us to understand in python
# print(type(soup.h1)) ... after the above step we look for the tag h1...

# print(soup.h1.string)
# print(type(soup.h1.string))...this last two is for gettin a string.stored in a tag in string format
#  

