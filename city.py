import time
from urllib import parse
import json
import traceback
import requests
from Base import Base
from lxml import etree


class CityList(Base):
    def sql_city(self, city_id, name, pinyin, acronym, rank, first_char):
        sql = 'insert into city_list(city_id, city_name, city_pinyin, city_acronym, city_rank, first_char) value({}, {}, {}, {}, {}, {})'.format(
            repr(city_id), repr(name), repr(pinyin), repr(acronym), repr(rank), repr(first_char)
        )
        try:
            print(sql)
            self.cursor.execute(sql)
            self.db_mysql.commit()
        except:
            traceback.print_exc()

    def get_appdata(self):
        url = 'https://www.meituan.com/changecity/'
        responsed = requests.get(url=url, headers=self.headers)
        html = etree.HTML(responsed.text)
        appdata = html.xpath("//script[contains(text(),'window.AppData')]/text()")
        if appdata:
            return appdata[0].replace("window.AppData = ", '')
        else:
            return False

    def get_citylist(self, appdata):
        appdata = parse.unquote(appdata[:-1])
        appdata = json.loads(appdata)
        # print(appdata)
        # print(type(appdata))
        list = appdata['openCityList']
        for fist_char_list in list:
            city_list = fist_char_list[1]
            for city in city_list:
                print(city)
                # id = '151'
                # name = '鞍山'
                # pinyin = 'anshan'
                # acronym = 'as'
                # rank = 'C'
                # fist_char = 'A'
                # self.sql_city(id, name, pinyin, acronym, rank, fist_char)
                self.sql_city(city['id'], city['name'], city['pinyin'], city['acronym'], city['rank'], city['firstChar'])



    def main(self):
        appdata = self.get_appdata()
        self.get_citylist(appdata)
        print('citylist 抓取完成')


if __name__ == '__main__':
    city_list = CityList()
    city_list.main()