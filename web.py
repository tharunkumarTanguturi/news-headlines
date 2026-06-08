import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

headlines = soup.find_all("span", class_="titleline")

with open("headline.txt", "w", encoding="utf-8") as f:
    for num, headline in enumerate(headlines, start=1):
        f.write(f"{num}. {headline.a.text}\n")

print("Headlines saved to headline.txt")