import requests
import xml.etree.ElementTree as ET
from typing import List
from bs4 import BeautifulSoup
from .rss_item import RSSItem


class RSSFeedParser:
    def __init__(self, url: str) -> None:
        self.url = url

    def fetch_feed(self) -> str:
        response = requests.get(self.url)
        response.raise_for_status()
        return response.text

    def parse_feed(self, raw_feed: str) -> List[RSSItem]:
        root = ET.fromstring(raw_feed)
        items = []

        for item in root.findall('.//item'):
            date = item.find('pubDate').text if item.find('pubDate') is not None else 'N/A'
            category = item.find('category').text if item.find('category') is not None else 'N/A'
            title = item.find('title').text if item.find('title') is not None else 'N/A'
            description_html = item.find('description').text if item.find('description') is not None else 'N/A'
            url = item.find('link').text if item.find('link') is not None else 'N/A'

            description = self._clean_html(description_html)

            rss_item = RSSItem(date, category, title, description, url)
            items.append(rss_item)

        return items

    def _clean_html(self, raw_html: str) -> str:
        soup = BeautifulSoup(raw_html, 'html.parser')
        return soup.get_text()
