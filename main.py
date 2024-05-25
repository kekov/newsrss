from rss_reader.rss_feed_parser import RSSFeedParser
from rss_reader.rss_reader import RSSReader



# rss_url = "https://services.lesechos.fr/rss/les-echos-tech-medias.xml"  # Remplacer par l'URL réelle du flux RSS
rss_url = "https://www.presse-citron.net/feed/"
parser = RSSFeedParser(rss_url)
reader = RSSReader(parser)

items = reader.get_items()
reader.display_items(items)