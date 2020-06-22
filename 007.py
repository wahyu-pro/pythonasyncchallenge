import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        data = await fetch(session, 'https://res.cloudinary.com/sivadass/raw/upload/v1535817394/json/products.json')
        result = list(filter(lambda a: a['category'] == "fruits", data))

        for i in result:
            print("{}, category: {}".format(i['name'], i['category']))

if __name__ == '__main__':
    asyncio.run(main())