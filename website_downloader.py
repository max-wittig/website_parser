import requests


class WebsiteDownloader:
    @staticmethod
    def download(url):
        r = requests.get(url)
        return r.text
