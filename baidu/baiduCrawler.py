# -*- coding: utf-8 -*-

from selenium import webdriver
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

browser = webdriver.PhantomJS()
url = 'https://www.baidu.com'
browser.get(url)
browser.implicitly_wait(3)
text = browser.find_element_by_id('kw')
text.clear()
text.send_keys('python')
button = browser.find_element_by_id('su')
button.submit()
print(browser.title)
browser.save_screenshot('text.png')
results = browser.find_elements_by_class_name('t')

for result in results:
    print('title:{} url:{}'.format(result.text, result.find_element_by_tag_name('a').get_attribute('href')))
