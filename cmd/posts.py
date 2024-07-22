# <h1 class="ts">
# <span id="thread_subject">女生會很敏感麻</span>
# </h1>
# <span class="xg1">
# <a href="thread-276681-1-1.html" onclick="return copyThreadUrl(this, '5278 / 5278論壇 / 我愛78論壇')" >[複製鏈接]</a>
# </span>
# </td>
# </tr>
import re

import requests
from bs4 import BeautifulSoup

# " id="postmessage_24837376

def getMessages(thread_url):
    base_url = thread_url[0]
    try:
        response = requests.get(thread_url)
    except requests.exceptions.RequestException as e:
        return ''
    response.encoding = 'utf-8'
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    td_tags = soup.find_all('td', id=re.compile(r'^postmessage_\d+'))

    tag_arr = []
    for td_tag in td_tags:
        tag_arr.append(td_tag.text)

    combined_text = str(tag_arr)
    # print(combined_text)
    return combined_text


def getSubject(thread_url):
    # try:
    #     response = requests.get(thread_url)
    # except requests.exceptions.RequestException as e:
    #     return ''
    # response.encoding = 'utf-8'
    # html_content = response.text
    # soup = BeautifulSoup(html_content, 'html.parser')
    # subject_tag = soup.find('span', id='thread_subject')
    # print(subject_tag.text)
    # return subject_tag.text.strip()
    return ''

def gettext(thread_url, nit):
    # print ('第' + str(nit) + '个网页:------------------------------------------')
    nit += 1
    return getMessages(thread_url) + getSubject(thread_url)
