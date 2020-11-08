from .settings import PROXIES


class DownloaderProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = "http://{}" .format(PROXIES[0])
        return None