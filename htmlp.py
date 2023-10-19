import requests as r
from  bs4 import BeautifulSoup as bs

class HtmlParser:
    def __init__(self, url:str):
        self.Url = url
        self.Counter = 0
        self.Result = {}

    def NbuParse(self, separator1:str, separator2:str):
        response = r.get(self.Url)
        response_content = response.content
        html = bs(response_content, features="html.parser")
        tags = html.find_all('div', attrs={'class':separator1})
        self.Result = {'usd':tags[3].text.strip()}