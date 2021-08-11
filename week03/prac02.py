import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#old_content > table > tbody > tr')

#old_content > table > tbody > tr:nth-child(2) > td.title > div > a
#old_content > table > tbody > tr:nth-child(3) > td:nth-child(1) > img
#old_content > table > tbody > tr:nth-child(2) > td.point


for tr in trs:
    title = tr.select_one('td.title > div > a')
    if title is not None:
        rank = tr.select_one('td:nth-child(1) > img')['alt']
        point = tr.select_one('td.point').text
        print(f"{rank:0>3s} {title.text} {float(point):<.2f}")
