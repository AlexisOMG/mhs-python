import aiohttp
import asyncio
import os
import argparse
import random

async def download_image(session: aiohttp.ClientSession, url: str, folder: str, file_name: str):
    async with session.get(url) as response:
        if response.status == 200:
            file_path = os.path.join(folder, file_name)
            with open(file_path, 'wb') as f:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f.write(chunk)
            print(f'Downloaded {file_name}')

async def run(num_files: int, folder: str):
    base_url = 'https://www.thiswaifudoesnotexist.net/example-{}.jpg'
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(num_files):
            random_id = random.randint(0, 100000)
            image_url = base_url.format(random_id)
            file_name = f'waifu_{random_id}.jpg'
            task = asyncio.ensure_future(download_image(session, image_url, folder, file_name))
            tasks.append(task)
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download the best waifus<3')
    parser.add_argument('--num_files', type=int, required=True, help='Number of waifus to download')
    parser.add_argument('--folder', type=str, required=True, help='Folder to save your waifus')
    args = parser.parse_args()

    asyncio.run(run(args.num_files, args.folder))
