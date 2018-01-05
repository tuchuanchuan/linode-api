# coding: utf-8

import sqlite3
import traceback

import requests
from scrapy.selector import Selector

def us_proxy(url, headers, f):
    r = requests.get(url, headers=headers)
    blocks = Selector(text=r.text).xpath("//table[@id='proxylisttable']//tbody//tr").extract()
    i = 0
    for block in blocks:
        info = Selector(text=block).xpath("//td/text()").extract()
        if info[4] == 'elite proxy':
            foo = "{}:{}\n".format(info[0], info[1])
            print foo
            proxies = {
                'https': 'https://{}'.format(foo.strip()),
            }
            print proxies
            try:
                requests.get('https://www.youtube.com/', proxies=proxies, timeout=3.0)
                f.write(foo)
                i += 1
                if i > 20:
                    break
            except:
                print traceback.format_exc()


if __name__ == '__main__':
    # url = "https://www.us-proxy.org/#myiphide"
    url = "https://www.sslproxies.org/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }

    with open('us-proxy', 'wb') as f:
        us_proxy(url, headers, f)
