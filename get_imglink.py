import requests
import urllib
import quote
from retrying import retry
from lxml import etree

@retry(stop_max_attempt_number=5)
def get_imglink(headers,url):
    r = requests.get(url+'list2/',headers=headers)
    html = etree.HTML(r.text)
    html_data = html.xpath('//*[@id="image-container"]/img[@class="list-img lazyload"]/@data-src')
    return html_data

if __name__ == "__main__":
    headers= {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
    print(get_imglink(headers,'https://zhb.eehentai.com/g/354876/'))
