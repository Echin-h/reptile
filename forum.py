from urllib.parse import urljoin


# 成人/秘密/糗事
# https://5278.cc/forum-219-20.html

def getForumUrl(base_url, index):
    n = str(index)
    path = 'forum-219-' + n + '.html'
    thread_url = urljoin(base_url, path)
    return thread_url
