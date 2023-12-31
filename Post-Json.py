# 导入模块
import requests
import time  # 时间戳内置模块

# 确定 url —— 动态加载
url = 'http://www.whggzy.com/front/search/category'

# 翻页获取数据
for i in range(1, 5):  # 左闭右开 1， 2， 3， 4
    # POST 请求传输数据，要携带参数
    data = {
        "utm":"sites_group_front.2ef5001f.0.0.ca79aa90f0c811edbc17f5eb8caaceab",
        "categoryCode":"GovernmentProcurement",
        "pageSize":15,
        "pageNo":i # 当前页码
    }

    # 发请求，获取响应
    res = requests.post(url, json=data)

    # 打印数据响应内容
    # print(res.text)

    # 数据解析
    result = res.json()['hits']['hits']
    # print(requests)

    # 遍历获取每一条数据
    for j in result:
        # print(j)
        source = j['_source']  # 获取包含标题和时间的数据
        title = source['title']  # 获取标题
        publishDate = source['publishDate']  # 获取时间，获取到的时间为13位时间戳
        times = time.localtime(publishDate / 1000)  # 13位时间戳转时间
        date = time.strftime("%Y-%m-%d %H:%M:%S", times) # 设置时间的格式
        print(title, date)  # 打印标题和时间