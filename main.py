import requests,threading,random
from fake_useragent import UserAgent

ua = UserAgent()
user_agent = ua.random

file = open('proxy.txt', 'r').read().splitlines()
proxies = {
    'http': f'{random.choice(file).__str__().strip()}',
    'https': f'{random.choice(file).__str__().strip()}'
}

def view():
    try: 
        headers = {
            'authority': 'api.e-z.bio',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'pl-PL,pl;q=0.8',
            'origin': 'https://e-z.bio',
            'referer': 'https://e-z.bio/',
            'sec-ch-ua': '"Brave";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'sec-gpc': '1',
            'user-agent': user_agent,
        }

        response = requests.put('https://api.e-z.bio/bio/view/ ur nick ', headers=headers, proxies=proxies)
        print(response.text)
    except Exception as e:
            pass
        
def start():
    while True:
        view()

for i in range(30):
    threading.Thread(target=start).start()
