from lxml import etree
import requests
import time
import os

class BaiduImageSpider:
    def __init__(self):
        self.baseurl = "https://tieba.baidu.com"
        self.headers = {"User-Agent":"Mozilla/5.0"}
        self.pageurl = "https://tieba.baidu.com/f?"
        
#    获取所有帖子URL列表
    def getPageUrl(self,params,foldername):
        res = requests.get(self.pageurl,params=params,headers=self.headers,timeout=5)
        res.encoding = "utf-8"
        html = res.text
        
        
        
        parseHtml = etree.HTML(html)
#        这里得到一个[/p/6395763211,/p/6607279013,/p/6625256353]这样的列表
        t_list = parseHtml.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
        
        for t_link in t_list:
            t_link = self.baseurl + t_link
            self.getImageUrl(t_link,foldername)
          
   
#    获取帖子中图片URL列表
    def getImageUrl(self,t_link,foldername):
        
        res = requests.get(t_link,headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        
        parseHtml = etree.HTML(html)
        img_list = parseHtml.xpath('//img[@class="BDE_Image"]/@src')
        for img_link in img_list:
            self.writeImage(img_link,foldername)
            
    def mkdir(self,name):
		#这里是设置爬取下来文件的保存路径，可以自行设置
        path = 'H:/爬虫学习/23-百度贴吧图片爬取/' + name + '/'
        floder = os.path.exists(path)
        if not floder:
            os.makedirs(path)
        else:
            pass
        foldername = path
        return foldername
    
#    保存到本地
    def writeImage(self,img_link,foldername):
        print(img_link)
        res = requests.get(img_link,headers=self.headers)
        res.encoding = "utf-8"
        html = res.content
        filename = foldername +img_link[-12:]
        with open(filename,"wb") as f:
            f.write(html)
            print("%s下载成功"% filename)
    
    def workOn(self):
        name = input("请输入贴吧名：")
        begin = int(input("请输入起始页："))
        end = int(input("请输入终止页："))
        foldername = self.mkdir(name)
        for n in range(begin,end+1):
            pn = (n-1)*50
            params = {
                    "kw":name,
                    "pn":str(pn)
                    }
            
            self.getPageUrl(params,foldername)
        
    
if __name__ == "__main__":
    spider = BaiduImageSpider()
    spider.workOn()
        
        
