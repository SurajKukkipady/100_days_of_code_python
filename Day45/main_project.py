import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
web_page = requests.get(URL)
print(web_page.status_code)  # Check if the request was successful (200 OK)

soup = BeautifulSoup(web_page.text, 'html.parser')

titles = soup.find_all('h3', class_='title')
title_list = [title.get_text() for title in titles]

# Reverse the list to get them from 1 to 100
title_list = list(reversed(title_list))

for title in title_list:
    print(title)

with open('movies.txt', 'w', encoding='utf-8') as f:
    for title in title_list:
        f.write(title + '\n')

# Write your code below this line 👇


