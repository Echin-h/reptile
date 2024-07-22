import re

from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import forum as forum
import posts

base_url = "https://5278.cc"
index = 20

# 帖子的URL
# base_url = 'https://5278.cc'
# thread_url = urljoin(base_url, 'forum-219-4.html')

thread_url = forum.getForumUrl(base_url, index)

# 发送HTTP请求
response = requests.get(thread_url)
response.encoding = 'utf-8'  # 根据响应内容设置正确的编码

html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

links = soup.find_all('a', href=True)

new_links = []

# n = 0
for link in links:
    if 'thread' in link['href']:
        new_link = urljoin(base_url, link['href'])
        # print(new_link)
        if new_link not in new_links:
            new_links.append(new_link)


print(new_links)
for new_link in new_links:
    ps = posts.gettext(new_link)
    print(ps)
