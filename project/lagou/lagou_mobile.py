# _*_ coding: utf-8 _*_

"""
title:抓取拉勾网的数据
time:2018-01-22
author:No.96
"""
import requests
import time
import random
import csv

# 移动端头部信息
from requests.cookies import RequestsCookieJar

useragents = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/47.0.2526.70 Mobile/13C71 Safari/601.1.46",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; Nexus 5 Build/KTU84P) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)",
    "Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36",
    "JUC (Linux; U; 2.3.5; zh-cn; MEIZU MX; 640*960) UCWEB8.5.1.179/145/33232",
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
]
cookies = {

}


# city城市
# positionName 职位关键字
# pageNo 页码
# pageSize 叶大小

def process_cookies(cookies):
    cookie_jar = RequestsCookieJar()
    lst1 = cookies.split(';')
    for item in lst1:
        cookie_jar.set(item.split('=')[0], item.split('=')[1])
    return cookie_jar


def lagou(city, positionName, pageNo, pageSize):
    cookies = "JSESSIONID=ABAAABAABEEAAJA9DBB4F5BE13CB68F1929E05076AA5976; user_trace_token=20180911093546-ea2b5f08-bc36-4a8b-92ea-3c8aa4ac96fc; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1536629748; _ga=GA1.2.526097846.1536629748; _gat=1; LGSID=20180911093547-01e5fb9f-b563-11e8-8e34-525400f775ce; PRE_UTM=; PRE_HOST=blog.csdn.net; PRE_SITE=https%3A%2F%2Fblog.csdn.net%2Fu012689336%2Farticle%2Fdetails%2F53170371; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_iOS%3Fpx%3Dnew%26city%3D%25E5%258C%2597%25E4%25BA%25AC; LGUID=20180911093547-01e5fe02-b563-11e8-8e34-525400f775ce; _gid=GA1.2.1306194661.1536629749; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1536629762; LGRID=20180911093601-0a636e7a-b563-11e8-8e34-525400f775ce; SEARCH_ID=8336a78dc3dc41f39a2d083a8a9967ad"
    cookie_jar = process_cookies(cookies)
    # req_url = "https://m.lagou.com/search.json?"
    # params = {
    #     "city": city,
    #     "positionName": positionName,
    #     "pageNo": pageNo,
    #     "pageSize": pageSize
    # }
    req_url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false'
    data = {
        'first': True,
        'pn': pageNo,
        'kd': positionName
    }
    # 请求头部
    headers = {
        # 'Host': 'm.lagou.com',
        'Origin': 'https://www.lagou.com',
        'X-Anit-Forge-Code': '0',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Cache-Control': 'no-cache',
        'Referer': 'https://www.lagou.com/jobs/list_iOS?px=new&city=%E4%B8%8A%E6%B5%B7',
        'X-Anit-Forge-Token': 'None',
        'User-Agent': random.choice(useragents)
    }
    res = requests.post(url=req_url, headers=headers,
                        data=data, cookies=cookie_jar)  # f发送请求
    res_json = res.json()  # 获取json数据
    if not res_json.get('success'):
        print(res_json)
    result = res_json['content']['positionResult']['result']
    return result  # 返回json数据


# 解析返回的json 并且保存
def write_to(result, writer):
    for item in result:
        job = {
            "city": item['city'],
            "companyFullName": item['companyFullName'],
            "companyName": item['companyShortName'],
            "positionName": item['positionName'],
            "salary": item['salary']
        }
        writer.writerow(job)


if __name__ == "__main__":
    city = "上海"
    positionNames = (
        # "Python",
        # "Angular",
        # "Golang",
        "区块链",
    )
    pageSize = 15
    for positionName in positionNames:
        filename = city + '_' + positionName + '.csv'
        with open(filename, 'a', encoding='utf-8') as f:
            fieldnames = ['city', 'companyFullName', 'companyName', 'positionName', 'salary']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(10):
                result = lagou(city, positionName, i + 1, pageSize)
                time.sleep(2)
                write_to(result, writer)
