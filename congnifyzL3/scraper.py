import requests
from bs4 import BeautifulSoup
import pandas as pd


class WebScraper:

    def __init__(self, url):
        self.url = url

        headers = {
            "User-Agent":
            "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()

        self.soup = BeautifulSoup(response.text, "lxml")

    def get_title(self):
        if self.soup.title:
            return self.soup.title.text.strip()
        return "No Title"

    def get_headings(self):

        headings = []

        for tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            for item in self.soup.find_all(tag):
                headings.append({
                    "Tag": tag.upper(),
                    "Text": item.get_text(strip=True)
                })

        return pd.DataFrame(headings)

    def get_links(self):

        links = []

        for link in self.soup.find_all("a", href=True):
            links.append({
                "Text": link.get_text(strip=True),
                "URL": link["href"]
            })

        return pd.DataFrame(links)

    def get_images(self):

        images = []

        for img in self.soup.find_all("img"):

            images.append({
                "Image": img.get("src"),
                "Alt": img.get("alt")
            })

        return pd.DataFrame(images)

    def get_paragraphs(self):

        paragraphs = []

        for p in self.soup.find_all("p"):

            text = p.get_text(strip=True)

            if text:
                paragraphs.append({
                    "Paragraph": text
                })

        return pd.DataFrame(paragraphs)

    def get_tables(self):

        try:
            tables = pd.read_html(str(self.soup))
            return tables
        except:
            return []