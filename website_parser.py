from website_downloader import WebsiteDownloader
from bs4 import BeautifulSoup
from urllib.parse import urljoin


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
            """element == tag --> e.g. img """
            self.html_tags_dict[element] = soup.find_all(element)
        self.complete_relative_url()

    def complete_relative_url(self):
        for key in self.html_tags_dict:
            for element in self.html_tags_dict[key]:
                href = element.get("href")
                src = element.get("src")
                data_src = element.get("data-src")
                data_src_high = element.get("data-src-high")
                if href is not None and href != "":
                    new_href = urljoin(self.properties.source_url, href)
                    element["href"] = element["href"].replace(href, new_href)
                if src is not None and src != "":
                    new_src = urljoin(self.properties.source_url, src)
                    element["src"] = element["src"].replace(src, new_src)
                if data_src is not None and data_src != "":
                    new_data_src = urljoin(self.properties.source_url, data_src)
                    element["data-src"] = element["data-src"].replace(data_src, new_data_src)
                if data_src_high is not None and data_src_high != "":
                    new_data_src_high = urljoin(self.properties.source_url, data_src_high)
                    element["data-src-high"] = element["data-src-high"].replace(data_src_high, new_data_src_high)
