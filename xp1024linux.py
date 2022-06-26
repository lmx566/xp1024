# -*- coding: UTF-8 -*-
#导入三方库
import os,requests,parsel,time
#链接变量
url = 'http://k11.1024xp1.xyz/pw/thread.php?fid=15&page=2'##+input('请输入您要下载的页数：')
print(url)
#定义头文件
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
#请求页面代码
response = requests.get(url=url,headers=headers)
#乱码处理
(type(response))
urls = ((response.text.encode(response.encoding).decode(response.apparent_encoding)))
#print(urls)
#转换类型xpath
selector = parsel.Selector(urls)
#print(selector)
#匹配Xpath规则
lis = selector.xpath('//div[@class= "t z"]/table/tbody/tr/td/h3')
#遍历页面下链接

###
for li in lis:
    time.sleep(1)
    pic_title = li.xpath('.//a/text()').get()
    time.sleep(1)
    pic_url = li.xpath('.//a/@href').get()
    print('正在下载相册' + pic_title)

#创建相册文件夹
    try:
        if not os.path.exists('img/' + pic_title):
            os.mkdir('img/' + pic_title)
    except:
        pass
    try:
        response_pic = requests.get('http://k11.csjbzcjnr.rocks/pw/'+pic_url,headers=headers)
        response_pict = response_pic.text
        selector_2 = parsel.Selector(response_pict)
        pic_url_list = selector_2.xpath('//div/img/@src').getall()
        #print(selector_2)
        #print(pic_url_list)
    except:
        pass
    for pic_url in pic_url_list:
        try:
            time.sleep(1)
            img_data = requests.get(url=pic_url,headers=headers).content
            file_name = pic_url.split('/')[-1]
            with open(f'img/{pic_title}/{file_name}', mode='wb') as f:
                f.write(img_data)
                print('保存完成：' + file_name)
        except:
            pass
exit()
