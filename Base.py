import pymysql

class Base():
    def __init__(self):
        pass

    #mysql链接
    db_mysql = pymysql.connect(host='43.132.250.79', port=3306, user='root', password='8888', database='meituan')
    cursor = db_mysql.cursor()

    #请求头
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Proxy-Connection': 'keep-alive',
        'Host': 'chs.meituan.com',
        'Referer': 'http://chs.meituan.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Content-Type': 'text/html;charset=utf-8',
        'Cookie': '_lxsdk_cuid=164c9bed44ac8-0bf488e0cbc5d9-5b193413-1fa400-164c9bed44bc8; __mta=248363576.1532393090021.1532393090021.1532393090021.1; rvct=70%2C1; ci=70; iuuid=30CB504DBAC7CCDD72645E3809496C48229D8143D427C01A5532A4DDB0D42388; cityname=%E9%95%BF%E6%B2%99; _lxsdk=30CB504DBAC7CCDD72645E3809496C48229D8143D427C01A5532A4DDB0D42388; _ga=GA1.2.1889738019.1532505689; uuid=2b2adb1787947dbe0888.1534733150.0.0.0; oc=d4TCN9aIiRPd6Py96Y94AGxfsjATZHPGsCDua9-Z_NQHsXDcp6WlG2x7iJpYzpSLttNvEucwm_D_SuJ7VRJkLcjqV6Nk8s_q3VyOJw5IsVJ6RJPL3qCgybGW3vxTkMHr9A4yChReTafbZ7f93F1PkCyUeFBQV4D-YXoVoFV5h3o; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; client-id=97664882-24cd-4743-b21c-d25de878708e; lat=28.189822; lng=112.97422; _lxsdk_s=165553df04a-bc8-311-ba7%7C%7C6',

    }
