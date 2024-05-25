class RSSItem:
    def __init__(self, date: str, category: str, title: str, description: str, url: str) -> None:
        self.date = date
        self.category = category
        self.title = title
        self.description = description
        self.url = url

    def __repr__(self) -> str:
        return f"RSSItem(date={self.date}, category={self.category}, title={self.title}, description={self.description}, url={self.url})"
