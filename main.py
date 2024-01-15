import requests
from bs4 import BeautifulSoup 

url = 'https://leetcode.com/problems/two-sum/'
headers = {'User-Agent':'Mozilla/5.0'}
res = requests.get(url=url, headers=headers)
if res.status_code == 200:
    sopa = BeautifulSoup(res.content, 'html.parser')
    