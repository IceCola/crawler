# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class Community:
    cmCount = 0

    def __init__(self, name, url):
        self.name = name
        self.url = url
        Community.cmCount += 1

    def displayCount(self):
        print "Total Community %d" % Community.empCount

    def displayCommunity(self):
        print "Name : ", self.name, ", Url: ", self.url

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap = {
    "phantomjs.page.settings.userAgent": "Mozilla/5.0 (Windows NT     10.0; WOW64) AppleWebKit/537.36 " \
                                        "(KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
    "phantomjs.page.settings.loadImages": False,
    "phantomjs.page.settings.resourceTimeout": 5000
}
browser = webdriver.PhantomJS(desired_capabilities=dcap)

distinct_urls = [
    'https://m.anjuke.com/sh/xiaoqu-pudong',
    'https://m.anjuke.com/sh/xiaoqu-minhang',
    'https://m.anjuke.com/sh/xiaoqu-baoshan',
    'https://m.anjuke.com/sh/xiaoqu-xuhui',
    'https://m.anjuke.com/sh/xiaoqu-songjiang',
    'https://m.anjuke.com/sh/xiaoqu-jiading',
    'https://m.anjuke.com/sh/xiaoqu-jingan',
    'https://m.anjuke.com/sh/xiaoqu-putuo',
    'https://m.anjuke.com/sh/xiaoqu-yangpu',
    'https://m.anjuke.com/sh/xiaoqu-hongkou',
    'https://m.anjuke.com/sh/xiaoqu-changning',
    'https://m.anjuke.com/sh/xiaoqu-huangpu',
    'https://m.anjuke.com/sh/xiaoqu-qingpu',
    'https://m.anjuke.com/sh/xiaoqu-fengxian',
    'https://m.anjuke.com/sh/xiaoqu-jinshan',
    'https://m.anjuke.com/sh/xiaoqu-chongming'
]

distList = []

for dist in distinct_urls:
    for i in range(1, 8):    # 网页上分页最多只返回7页内容
        distUrl = dist + '-p' + str(i)
        browser.get(distUrl)
        # browser.implicitly_wait(1)
        items = browser.find_elements_by_class_name('items')[0].find_elements_by_tag_name('a')
        itemCnt = 1
        for result in items:
            print "add dist page: " + str(i) + " item: " + str(itemCnt) + "/" + str(len(items))
            # print('title:{} url:{}'.format(result.text, result.get_attribute('href')))
            distList.append(Community(result.text, result.get_attribute('href')))
            itemCnt += 1

pattern = re.compile(ur'^.*?地址：(.{2})(.{2})(.*?)。为您提供.*$')

output = open("output.txt", "a")
outCnt = 1
for dist in distList:
    browser.get(dist.url)
    # browser.implicitly_wait(1)
    address_description_info = browser.find_element_by_id('seo-description-info').text
    address = re.sub(pattern, r'\1市\2区\3', address_description_info)
    address = address.replace('浦东区','浦东新区')
    print "write output " + str(outCnt) + "/" + str(len(distList)) + " " + dist.name
    output.write(dist.name + ',' + dist.url + ',' + address)
    output.write('\n')
    outCnt += 1