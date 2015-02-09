#coding=utf-8

'''
input: xml with particular DTD
output: the data_set in the xml
'''

import re
from student_info import sc

def get_data(file_path):
    sc_list = []
    avl = open(file_path, 'rb')
    str_tmp = avl.read()
    avl.close()
    #print str_tmp
    scourse = re.findall(r'<!ELEMENT (\w+)\([^#].+\)>',str_tmp)
    remine = list()
    result = list()
    for s in scourse:
        tmp = r'<%s>(.+?)</%s>'%(s,s)
        remine.append(re.compile(tmp,re.DOTALL))
        
    scour = re.findall(r'<!ELEMENT (\w+)\(#\w+\)>',str_tmp)
    for si in scour:
        s_temp = r'<%s>(.+?)</%s>'%(si,si)
        result.append(re.compile(s_temp,re.DOTALL))



    scourse_list = remine[0].findall(str_tmp)

    for idx,item in enumerate(scourse_list):
        s_name = result[0].findall(item)
        s_id = result[1].findall(item)
        s_grade = result[2].findall(item)
        s_cid = result[3].findall(item)
        s_cname = result[4].findall(item)
        s_teacher = result[5].findall(item)
        s_cscore = result[6].findall(item)
            
        sc_list.append(sc(s_name,s_id,s_grade,s_cid,s_cname,s_teacher,s_cscore,idx+1))
    return sc_list
    
if __name__ == "__main__":
    scourse_list = get_data('sc_info.xml')
    
    for sc in scourse_list:
        sc.print_info()
    

   
