import aiohttp 

class reqs:
    """Methods to handle requests"""

    @classmethod ## creating one instance for all requests
    def ses(self):
        self.ses = aiohttp.ClientSession()
        return self.ses

    @staticmethod ## check for headers
    def header_check(headers: any = None):
        if not headers:
            headers = {}
        else:
            headers = {headers}

        return headers

    @staticmethod ## check for data {PUT & POST} 
    def data_check(data: any = None):
        if not data:
            data = {}
        else:
            data = {data}

        return data

    @classmethod ## GET request
    async def get(self, url: str, *, headers: any = None):
        headers = reqs.header_check(headers)
        ses = reqs.ses()
        async with ses.get(url, headers=headers) as r:
            if r.status in range(200, 299):
                data = await r.json()
                return data
            else:
                return r.status
        
        @classmethod ## POST request
        async def post(self, url: str, *, headers: any = None, data: any = None):
            headers = reqs.header_check(headers)
            data = reqs.data_check(data)
            ses = reqs.ses()
            async with ses.post(url, headers=headers, data=data) as r:
                if r.status in range(200, 299):
                    data = await r.json()
                    return data
                else:
                    return r.status

        @classmethod ## PUT request
        async def put(self, url: str, *, headers: any = None, data: any = None):
            headers = reqs.header_check(headers)
            data = reqs.data_check(data)
            ses = reqs.ses()
            async with ses.put(url, headers=headers, data=data) as r:
                if r.status in range(200, 299):
                    data = await r.json()
                    return data
                else:
                    return r.status

