from lxml import etree
from parser_properties import ParserProperties
from website_downloader import WebsiteDownloader


class WebsiteParser:
    """downloads DOM from website and parses it to use with the website_generator"""
    def __init__(self, properties):
        self.downloader = WebsiteDownloader()
        print(self.downloader.download(properties.source_url))

        #self.parser = etree.HTMLParser()
        #self.tree = self.parser.parse
        pass
