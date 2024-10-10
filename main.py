import requests

url = "https://www.kdnuggets.com/"
res = requests.get(url)
htmlData = res.content
print(htmlData)