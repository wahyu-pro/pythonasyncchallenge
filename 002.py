import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        data = await fetch(session, 'https://jsonplaceholder.typicode.com/users')
        result = map(lambda a: "alamat {}, {}, {} ".format(a['address']['street'], a['address']['city'], a['address']['suite']), data)
        for i in result:
            print(i)

if __name__ == '__main__':
    asyncio.run(main())