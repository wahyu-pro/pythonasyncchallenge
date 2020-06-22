import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        data = await fetch(session, 'https://api.themoviedb.org/3/movie/top_rated?api_key=6ee5671a60dffcfba9b370c145061ef8')
        result = map(lambda a: "title : {} - vote : {}".format(a['title'], a['vote_average']), data['results'])
        for i in result:
            print(i)

if __name__ == '__main__':
    asyncio.run(main())