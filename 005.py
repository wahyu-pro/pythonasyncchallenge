import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        data = await fetch(session, 'https://api.themoviedb.org/3/movie/top_rated?api_key=6ee5671a60dffcfba9b370c145061ef8')
        result = filter(lambda a: a['vote_average'] >= 8.4, data['results'])
        res = map(lambda a: "{}, vote: {}".format(a['title'], a['vote_average']), result)
        for i in res:
            print(i)

if __name__ == '__main__':
    asyncio.run(main())