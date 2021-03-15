import aiohttp 

class reqs:
    
    @classmethod
    async def ses(self):
        self.ses = aiohttp.ClientSession()
        return self.ses

    @classmethod
    async def get(self, url: str, *, headers: any = None):
        if not headers:
            headers = {}
        elif headers:
            headers = {
                headers
            }
            
        async with reqs.ses.get(url, headers=headers) as r:
            if r.status in range(200, 299):
                data = await r.json()
                return data
            else:
                return r.status
        
        @classmethod
        async def post(self, url: str, *, headers: any = None, data: any = None):
            if not headers:
                headers = {}
            elif headers:
                headers = {
                    headers
                }

            if not data:
                data = {}
            elif data:
                data = {
                    data
                }
                
            async with reqs.ses.post(url, headers=headers, data=data) as r:
                if r.status in range(200, 299):
                    data = await r.json()
                    return data
                else:
                    return r.status
        
        @classmethod
        async def put(self, url: str, *, headers: any = None, data: any = None):
            if not headers:
                headers = {}
            elif headers:
                headers = {
                    headers
                }

            if not data:
                data = {}
            elif data:
                data = {
                    data
                }

            async with reqs.ses.put(url, headers=headers, data=data) as r:
                if r.status in range(200, 299):
                    data = await r.json()
                    return data
                else:
                    return r.status
        