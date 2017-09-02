#coding:utf-8

import codecs

file_object = codecs.open('c:/temp/site3_0901_72986.csv','r','utf-8')
out1 = codecs.open('c:/temp/11.csv','wb')

list_of_all_the_lines = file_object.readlines( )

for line in list_of_all_the_lines:
    #print(line)
    line1 = line.encode('gbk','ignore')
    #print(line1)
    print('.',end='')
    out1.write(line1)
    #break

file_object.close()
out1.close()
