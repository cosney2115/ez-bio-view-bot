import random,threading

from curl_cffi import requests
from loguru import logger

class EzBio:
    def __init__(self, proxies: list):
        self.session = requests.Session()

        self.session.headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'pl-PL,pl;q=0.6',
            'origin': 'https://e-z.bio',
            'priority': 'u=1, i',
            'referer': 'https://e-z.bio/',
            'sec-ch-ua': '"Brave";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'sec-gpc': '1',
        }

    def get_random_proxy(self):
        return random.choice(proxies)
    
    def get_random_useragent(self):
        return f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.{random.randint(1000, 4000)}.0 Safari/537.36'

    def send_views(self, username: str):
        useragent = self.get_random_useragent()

        self.session.headers['user-agent'] = useragent

        proxy = self.get_random_proxy()
        proxies = {
            'http': 'http://'+proxy,
            'https': 'http://'+proxy
        }

        response = self.session.put(f'https://api.e-z.bio/bio/view/{username}', impersonate="edge101", proxies=proxies)
        if not response.json()['success']:
            logger.error('Failed to send view')
            return
        
        logger.success(f'View sent successfully to {username}')

    def start(self, username: str):
        while True:
            self.send_views(username)

proxies = open('proxy.txt', 'r').read().splitlines()
ezbio = EzBio(proxies)
username = input('Enter username: ')
threads = int(input('Enter number of threads: '))

for _ in range(threads):
    threading.Thread(target=ezbio.start, args=(username,)).start()
