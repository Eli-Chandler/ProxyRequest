import aiohttp

class Session:
    session = None
    def __init__(self, proxy_url):
        self.proxy_url = proxy_url

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()

    async def __aexit__(self):
        await self.session.close()

    async def get(self, url, **kwargs):
        payload = {
            'method': 'GET',
            'url': url,
            'headers': kwargs.get('headers'),
            'cookies': kwargs.get('cookies'),
            'params': kwargs.get('params'),
            'data': kwargs.get('data'),
            'json': kwargs.get('json', None),
        }
        async with self.session.post(self.proxy_url, json=payload) as response:
            return response

    async def post(self, url, **kwargs):
        payload = {
            'method': 'POST',
            'url': url,
            'headers': kwargs.get('headers'),
            'cookies': kwargs.get('cookies'),
            'params': kwargs.get('params'),
            'data': kwargs.get('data'),
            'json': kwargs.get('json', None),
        }
        async with self.session.post(self.proxy_url, json=payload) as response:
            return response