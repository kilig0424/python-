# -*- coding: utf-8 -*-
"""
Created on Tue May 19 09:16:22 2020

@author: Administrator
"""

import csv
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#import time


#读取文档中的数据
file = 'F:\csv519.csv'
start_n = int(input("请输入起始行："))
end_n = int(input("请输入结束行："))

#利用爬虫来获取回放链接
#def log_in():
##    opt = webdriver.ChromeOptions()
##    opt.set_headless()
#   # 创建浏览器对象,发请求
#    driver = webdriver.Chrome()
#    driver.get("http://vip.51cth.com") 
#    # 找 用户名、密码、验证、登陆豆瓣按钮
#    uname = driver.find_element_by_name("userName")
#    uname.send_keys("51cth")
#    # 密码
#    pwd = driver.find_element_by_name("password")
#    pwd.send_keys("123456")
#    time.sleep(3)
#    # 点击登陆按钮
#    login = driver.find_element_by_class_name("input-submit.large")
#    login.click()
#    driver.save_screenshot("登陆成功.png")
#    
##    点击直播后台按钮
#    head_open = driver.find_element_by_id("head_open_live")
#    head_open.click()
#    driver.save_screenshot("挑战到直播后台.png")
#    # 关闭浏览器
#    driver.quit()
        
    


def get_file(file):
    with open(file,'r',newline='') as f:
        reader = csv.reader(f)
        list = []
        for row in reader:
            list.append(row)
    return list
    

def set_file(list):
    list_all = []    
    for i in range(start_n-1,end_n+1):
        for j in range(8,26):
            list_s = []
    #    幼儿园名称
            k_name = list[i][1]
        #    日期
            c_date = list[i][0]
        #    时间 
            c_time = list[1][j]
    #        班级
            c_class =list[i][j]
    #        老师
            c_teacher = list[i][4]
    #        print(c_teacher)
            if c_class != '':
                list_s.append(k_name)
                list_s.append('上课日期:'+c_date)
                list_s.append('课程时间:'+c_time)
                list_s.append('上课班级:'+c_class)
                list_s.append('上课老师:'+c_teacher)
                list_s.append('回放链接：')
                list_s.append('\n')
                list_all.append(list_s)
#    print(list_all)
    return list_all
    
    
def write_file(list_all):
    with open('520txt文件.txt','w',newline='\n') as f:
        for i in list_all:
            for j in i:
                f.write(j)           
                f.write('\n')
                
def run():
    list = get_file(file)
    list_all = set_file(list)
    write_file(list_all)
#    log_in()
                
                
if __name__ == "__main__":
    run()
       
    

    
