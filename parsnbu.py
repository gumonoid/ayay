import requests
from htmlp import HtmlParser

parser = HtmlParser("https://bank.gov.ua/")
parser.NbuParse('index-page', 'small')

print(f"Курс долара - {parser.Result} гривень")

number = (int(input("Скільки ви хочете конвертувати: ")))

print(f"{number} доларів = {number * 36.5} гривень")