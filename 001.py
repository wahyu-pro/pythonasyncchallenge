import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        data = await fetch(session, 'https://jsonplaceholder.typicode.com/posts')
        result = list(map(lambda a: a['title'], data))
        for i in result:
            print("Title : ", i)

if __name__ == '__main__':
    asyncio.run(main())

