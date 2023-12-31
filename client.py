import asyncio
import httpx
import time


async def get_data_api(city: str):
    url = f'http://127.0.0.1:8000/api/weather/{city}'

    for i in range(6):
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()

        data = response.json()
        print('city: {}, temp: {}, src: {}'.format(
            data.get('city'), data.get('temp'), data.get('src')
        ))


async def main():
    tasks = [asyncio.create_task(get_data_api('moskva')),
             asyncio.create_task(get_data_api('voronezh')),
             asyncio.create_task(get_data_api('tokyo')),
             asyncio.create_task(get_data_api('london'))]

    await asyncio.gather(*tasks)


start = time.time()
asyncio.run(main())
end = time.time() - start
print(f'time {end:0.2f} seconds')
print(f'mean time for 1 request {end/18:0.2f} seconds')

# start = time.time()

# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# loop.run_until_complete(asyncio.gather(*tasks))
# loop.close()

# end = time.time() - start
# print(f'time {end:0.2f} seconds')
# print(f'mean time for 1 request {end/18:0.2f} seconds')
