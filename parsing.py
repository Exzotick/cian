from bs4 import BeautifulSoup
import requests
import time
import socks
import socket
from random import randint
from fake_useragent import UserAgent
UserAgent().chrome


# socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
# socket.socket = socks.socksocket
# def checkIP():
#     ip = requests.get('http://checkip.dyndns.org').content
#     soup = BeautifulSoup(ip, 'html.parser')
#     print(soup.find('body').text)

search = 'https://www.cian.ru/cat.php?deal_type=rent&engine_version=2&foot_min=20&mebel=1&mebel_k=1&offer_type=flat&only_foot=2&p={}&region=1&rfgr=1&room1=1&room9=1&type=-2&wm=1'
first_page = search.format('1')
first_response = requests.get(first_page, headers={'User-Agent': UserAgent().chrome})
first_html = first_response.content
first_soup = BeautifulSoup(first_html, 'html.parser')
offers_info = first_soup.find('div', attrs={'class': '_93444fe79c--totalOffers--22-FL'})
time.sleep(15)
for key, value in first_response.request.headers.items():
    print(key+": "+value)

num_pages = 15
flat_links = []
search_pages_soup = []
for page_iter in range(1, num_pages+1):
    search_page = search.format(str(page_iter))
    search_response = requests.get(search_page, headers={'User-Agent': UserAgent().chrome})
    print(search_response)
    search_html = search_response.content
    search_soup = BeautifulSoup(search_html, 'html.parser')
    search_pages_soup.append(search_soup)
    main_info = search_soup.find_all('div', attrs={'class': ["undefined c6e8ba5398--main-info--oWcMk", 
                                                            "c6e8ba5398--info-section--Sfnx- c6e8ba5398--main-info--oWcMk"]                    })
    print(page_iter,'/',num_pages, len(main_info))
    time.sleep(randint(12, 62))
    # page_links = [ad.a.attrs['href'] for ad in main_info]
    # flat_links.extend(page_links)
    # print(flat_links)
    # print(len(flat_links))
    # print(flat_links[])

# flats = []
# count = 0
# for flat_page in flat_links:
#     count = count + 1
#     print(count)
#     flat_id = flat_page.split('/')[-2]
#     print(flat_id)
#     flat_response = requests.get(flat_page)
#     flat_html = flat_response.content
#     flat_soup = BeautifulSoup(flat_html, 'html.parser')
#     pay_info = flat_soup.find('span', attrs={'class': 'a10a3f92e9--price_value--1iPpd'})
#     price = pay_info.find('span', attrs={'itemprop': 'price'})['content'].split()[0]
#     currency = pay_info.find('span', attrs={'itemprop': 'priceCurrency'})['content']
#     bills = flat_soup.find('div', attrs={'class': 'a10a3f92e9--more_price_rent---5hwY'}).text
#     deal_info = flat_soup.find('p', attrs={'class': 'a10a3f92e9--description--2xRVn'}).text
#     print(price, currency)
#     print(bills)
#     deal_info = flat_soup.find('p', attrs={'class': 'a10a3f92e9--description--2xRVn'}).text
#     print(deal_info)

#     station = flat_soup.find('a', attrs={'class': 'a10a3f92e9--underground_link--AzxRC'}).text
#     walk_time_info = flat_soup.find('span', attrs={'class': 'a10a3f92e9--underground_time--1fKft'})
#     if walk_time_info is not None:
#         walk_time = walk_time_info.text
#     else:
#         walk_time = None
#     # print(station, walk_time)

#     building_params = [item.text for item in flat_soup.find_all('div', attrs={'class': 'a10a3f92e9--name--22FM0'})]
#     building_values = [item.text for item in flat_soup.find_all('div', attrs={'a10a3f92e9--value--38caj'})]
#     building_info = dict(zip(building_params, building_values))
#     # print(building_info)

#     space_params = [item.text for item in flat_soup.find_all('span', attrs={'class': 'a10a3f92e9--name--3bt8k'})]
#     space_values = [item.text for item in flat_soup.find_all('span', attrs={'class': 'a10a3f92e9--value--3Ftu5'})]
#     space_info = dict(zip(space_params, space_values))
#     # print(space_info)
#     flat_info = (flat_id, price, currency, bills, deal_info, station, walk_time, building_info, space_info)
#     flats.append(flat_info)
# # print(flats)