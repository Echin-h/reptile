import time

from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import posts, forum
import save

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

n = 1

for link in links:
    if 'thread' in link['href']:
        new_link = urljoin(base_url, link['href'])
        # print(new_link)
        if new_link not in new_links:
            new_links.append(new_link)

print(new_links)
save_links = []
for new_link in new_links:
    try:
        time.sleep(2)  # 爬虫爬的慢一点，不然会被封IP
        ps = posts.gettext(new_link, n)
        print(ps)
        words = [ps]
        if not words:
            continue
        # break
        save_links.append(words)

        n += 1
    except Exception as e:
        # print(ps)
        # n += 1
        time.sleep(5)
        continue

try:
    save.write_to_csv(save_links, './data.csv', False)
except Exception as e:
    print(e)
