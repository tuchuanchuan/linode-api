import logging
import random
import time
import traceback
import urllib
import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType

dc = DesiredCapabilities.FIREFOX.copy()
# import ipdb; ipdb.set_trace()
# profile = webdriver.FirefoxProfile()
# profile.set_preference("general.useragent.override", "whatever you want")
# driver = webdriver.Firefox(profile)
# driver.get("http://127.0.0.1:8888/")

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

user_agents = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/7.0.5 Safari/537.77.4",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:17.0) Gecko/20100101 Firefox/17.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
]


def get_random_proxy():
    proxies = json.loads(urllib.urlopen('http://173.230.151.140:22345/proxy/checked/list?protocol=https').read())
    return ':'.join(random.choice(proxies['proxy_list'])[:2])


while True:
    try:
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", random.choice(user_agents))
        random_proxy = get_random_proxy()
        print random_proxy
        proxy = Proxy({
            'proxyType': ProxyType.MANUAL,
            'httpProxy': random_proxy,
            'ftpProxy': random_proxy,
            'sslProxy': random_proxy,
            'noProxy': '' # set this value as desired
        })
        driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            # command_executor='http://80.85.85.190:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX,
            browser_profile=profile,
            proxy=proxy,
        )
        random_list = ['https://www.youtube.com/watch?v=lHYKSTROp8o', 'https://www.youtube.com/watch?v=rRzxEiBLQCA', 'https://www.youtube.com/watch?v=-tKVN2mAKRI', 'https://www.youtube.com/watch?v=pC7a27zE2fs', 'https://www.youtube.com/watch?v=wnJ6LuUFpMo', 'https://www.youtube.com/watch?v=Amq-qlqbjYA', 'https://www.youtube.com/watch?v=5ZwctAeWrVs', 'https://www.youtube.com/watch?v=UceaB4D0jpo', 'https://www.youtube.com/watch?v=sV2t3tW_JTQ']
        target = 'https://www.youtube.com/watch?v=4a2RnnMIvK0'
        driver.get(random.choice(random_list))
        time.sleep(random.random()*3)
        driver.get(random.choice(random_list))
        time.sleep(random.random()*7)
        driver.get(target)
        print '--------page got---------'
        time.sleep(random.random()*400+ 20)
        driver.close()
    except KeyboardInterrupt as e:
        raise
    except:
        print traceback.format_exc()
