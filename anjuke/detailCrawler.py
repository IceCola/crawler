# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# data = open('resource/community.csv', 'r')
# output = open("resource/solr_data.json", "a")
data = open('resource/community_test.csv', 'r')
output = open("resource/solr_data_test.json", "a")


for line in data.readlines():
    entity = line.strip('\n').split(',')
    if len(entity) < 3:
        pass
    title = entity[0]
    url = entity[1]
    if len(entity) > 3:
        address = line.replace(entity[0] + ',' + entity[1] + ',', '')
    else:
        address = entity[2]
    content = address + " " + title
    output.write(
        '{"title":"' + title + '","url":"' + url + '","address":"' + address + '","content":"' + content + '"}')
    output.write('\n')
output.close()
