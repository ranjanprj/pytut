import requests
from bs4 import BeautifulSoup

bse_site =  'https://www.hindustantimes.com/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}


bse_site = requests.get(bse_site, headers=headers, timeout=10, verify=False)


bse_web_site_text = bse_site.text
soup = BeautifulSoup(bse_web_site_text, 'html.parser')

articles = soup.find_all(class_="hdg3")

for article in articles:
    print("============================")
    a = article.find("a")
    news_link = a.attrs['href']

    # again call requests.get on the news_link

    # push the html into bs4

    # again parse and display the 


    


