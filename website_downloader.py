import urllib3


class WebsiteDownloader:
    def __init__(self):
        self.http = urllib3.PoolManager()

    def download(self, url):
        request = self.http.request('GET', url)
        return request.data
