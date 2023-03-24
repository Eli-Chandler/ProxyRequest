import aiohttp

class Session:
    session = None
    def __init__(self, proxy_url):
        self.proxy_url = proxy_url

    async def setup(self):
        self.session = aiohttp.ClientSession()

    async def close(self):
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
        r = await self.session.post(self.proxy_url, json=payload)
        return r

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
        r = await self.session.post(self.proxy_url, json=payload)
        return r

async def main():
    s = Session('http://localhost:5000')
    await s.setup()
    r = await s.get('https://www.youtube.com')
    print(await r.text())

if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
