from random import randint
import time
import socks
import socket
from scipy.stats import expon
import requests
from bs4 import BeautifulSoup

from fake_useragent import UserAgent


search = '''https://www.cian.ru/cat.php?deal_type=rent&
            engine_version=2&foot_min=20&mebel=1&mebel_k=1&offer_type=flat&
            only_foot=2&p={}&region=1&rfgr=1&room1=1&room9=1&type=-2&wm=1'''
first_page = search.format('1')
first_response = requests.get(first_page, 
                              headers={'User-Agent': UserAgent().chrome}
                              )
first_html = first_response.content
first_soup = BeautifulSoup(first_html, 'html.parser')
offers_info = first_soup.find('div', 
                              attrs={'class': '_93444fe79c--totalOffers--22-FL'}
                              )
time.sleep(expon.rvs(30, 10))
main_info = first_soup.find('div', 
                            attrs={'class': [
                                            'c6e8ba5398--title--2CW78',
                                            'c6e8ba5398--subtitle--UTwbQ',
                                            'c6e8ba5398--single_title--22TGT'
                                            ]
                                  }   
                            )

print(main_info.text)
num_pages = 9
flat_links = []
main_info_list = []
for page_iter in range(1, num_pages+1):
    search_page = search.format(str(page_iter))
    search_response = requests.get(search_page, 
                                   headers={'User-Agent': UserAgent().chrome}
                                   )
    # print(search_response)
    search_html = search_response.content
    search_soup = BeautifulSoup(search_html, 'html.parser')
    main_info = search_soup.find_all('div', 
                                     attrs={'class': [
                                                     'c6e8ba5398--title--2CW78',
                                                     'c6e8ba5398--subtitle--UTwbQ',
                                                     'c6e8ba5398--single_title--22TGT'
                                                     ]
                                            }
                                    )
    station_info = search_soup.find_all('div',
                                        attrs={'class': 'c6e8ba5398--underground-name--3YjAi'}
                                        )
    # search_pages_soup.append(search_soup)                  
    print(page_iter,'/',num_pages, len(station_info))
    # print(main_info[0].text)
    # time.sleep(randint(22, 57))