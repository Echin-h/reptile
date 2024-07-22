import random
import time

from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import posts, forum
import save

base_url = "https://5278.cc"
# index = 20

# 帖子的URL
# base_url = 'https://5278.cc'
# thread_url = urljoin(base_url, 'forum-219-4.html')
index = 21
filepath = './data' + str(index) + '.csv'

with open(filepath, 'w') as file:
    pass

for index in range(21, 41):
    thread_url = forum.getForumUrl(base_url, index)

    # 发送HTTP请求
    response = requests.get(thread_url, timeout=10)
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
    n = 1
    for new_link in new_links:
        try:
            # time.sleep()  # 爬虫爬的慢一点，不然会被封IP
            ps = posts.gettext(new_link, n)
            print(ps)
            words = [ps]
            # if not ps:
            #     continue
            if words:
                save_links.append(words)
            # break
            n += 1
            time.sleep(random.randint(1,3))
        except Exception as e:
            time.sleep(random.randint(3,7))
            continue

    # n = 1
    # for new_link in new_links:
    #     try:
    #         ps = posts.gettext(new_link,n)
    #         n += 1
    #         words = [ps]
    #         if words:
    #             save_links.append(words)
    #     except Exception as e:
    #         print(f"Error processing {new_link}: {e}")
    #         continue

    # path = './data' + str(index) + '.csv'
    #
    # with open(path, 'w') as file:
    #     pass
    # 写入一些内容到文件中，这里只是一个示例

    path = './data' + str(index) + '.csv'

    try:
        save.write_to_csv(save_links, path, False)
    except Exception as e:
        print(e)

    print("第" + str(index) + "页爬取完-----------------------------------------------------------------")
