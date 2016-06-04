from parser_properties import ParserProperties
from website_downloader import WebsiteDownloader
from website_generator import WebsiteGenerator
from bs4 import BeautifulSoup


class WebsiteParser:
    """downloads DOM from website and parses it to use with the website_generator"""
    def __init__(self, properties):
        self.properties = properties
        self.downloader = WebsiteDownloader()
        self.html = self.downloader.download(properties.source_url)
        self.html_tags_dict = dict()
        self.parse()

    def parse(self):
        """parses website and extracts specific tags in html_tag class"""
        soup = BeautifulSoup(self.html, "html.parser")
        for element in self.properties.tags_to_download:
            self.html_tags_dict[element] = soup.find_all(element)
