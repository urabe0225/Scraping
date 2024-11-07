import requests
from bs4 import BeautifulSoup

url = "https://www.tis.co.jp/news/index.html"
res = requests.get(url)
html = res.text
parse_html = BeautifulSoup(res.text, "html.parser")
print(parse_html.prettify())
title_lists = parse_html.find_all("li")
print(title_lists)