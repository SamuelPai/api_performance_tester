import requests
import concurrent
from concurrent.futures import ThreadPoolExecutor
import time
characters = range(1, 10)
base_url = 'https://rickandmortyapi.com/api/character'
threads = 20

def get_character_info(character):
    headers = {"Authorization": "Bearer MYREALLYLONGTOKENIGOT"}
    r = requests.get(f'{base_url}/{character}')
    return r.json()

with ThreadPoolExecutor(max_workers=threads) as executor:
    start_time = time.time()
    future_to_url = {executor.submit(get_character_info, char)
    for char in characters}
    for future in concurrent.futures.as_completed(future_to_url):
        try:
            data = future.result()
            print(data)
        except Exception as e:
            print('Looks like something went wrong:', e)
    print("--- %s seconds ---" % (time.time() - start_time))
    # 0.9544878005981445