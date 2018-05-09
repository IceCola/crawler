# -*- coding: utf-8 -*-

import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
data = open('resource/main.json', 'r')
output = open("resource/output.txt", "a")

pattern = re.compile(ur'\[([^,^\[]*?),"([^,]*?)",(.*?)\]')
results = pattern.findall(data.read())
for result in results:
    output.write(result[1])
    output.write('\n')
data.close()
output.close()