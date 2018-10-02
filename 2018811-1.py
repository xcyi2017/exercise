import re
import requests
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False   # 步骤二（解决坐标轴负数的负号显示问题）


class Game():

    def __init__(self):
        self.url = 'http://pubgm.qq.com/zlkdatasys/a20171229jdcs/list.shtml'
        self.response = requests.get(self.url)
        html = self.response.content.decode('gbk')


        self.name = re.findall(r'<div class="qx_tab_name">(.*?)</div>', html,re.S)[1:8]
        self.per_url = re.compile(r'<a href="(.*?)" target="_blank" class="btn_xq datum_list_sp"').findall(html)[:7]

        self.data = []
        for li in self.per_url:
            li = 'http://pubgm.qq.com'+ li
            a = requests.get(li).text
            arg = re.compile(r'<span style="width:(.*?)%;"></span>').findall(a)
            self.data.append(arg)

        dic_G = dict(zip(self.name,self.data))

        self.to_csv = pd.DataFrame(dic_G,index=['射速','威力','射程','稳定'],dtype='float')
        print(self.to_csv)
        self.to_csv.plot(kind='bar',subplots=True,layout=(3,3),legend=False,rot=0)
        plt.tight_layout()
        plt.show()




if __name__ == '__main__':
    game = Game()