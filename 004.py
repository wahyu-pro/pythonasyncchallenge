import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        data = await fetch(session, 'https://jsonplaceholder.typicode.com/users')
        result1 = filter(lambda a: 'le' in a['name'].lower(), data)
        result = map(lambda a: a['name'], result1)
        for i in result:
            print(i)

if __name__ == '__main__':
    asyncio.run(main())