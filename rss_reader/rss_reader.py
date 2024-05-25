from typing import List
from .rss_feed_parser import RSSFeedParser
from .rss_item import RSSItem

class RSSReader:
    def __init__(self, parser: RSSFeedParser) -> None:
        self.parser = parser

    def get_items(self) -> List[RSSItem]:
        raw_feed = self.parser.fetch_feed()
        return self.parser.parse_feed(raw_feed)

    def display_items(self, items: List[RSSItem]) -> None:
        for item in items:
            print(item)