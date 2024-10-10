from bs4 import BeautifulSoup
import requests

url = "https://www.kdnuggets.com/"
res = requests.get(url)
htmlData = res.content
# print(htmlData)

# //to this point, we extract raw html content.Text , paragraphs,anchortags,divs..all ..next task is to parse data for text and tags separately//
# //un comment print(htmlData)..to validate the above step..

parsedData = BeautifulSoup(htmlData, "html.parser")
print(parsedData.prettify())