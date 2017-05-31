#coding=utf8
import re
import os
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
# print sys.getdefaultencoding()
def save_result_to_file(keyword, result_list, result_dir):
    file_name = re.sub(r'[#$%％&\'()*+,-./_：: ]', '_', keyword.strip())  + '.txt'
    print file_name
    # file_name=file_name.decode('ascii')
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    result_file = os.path.join(result_dir, file_name)
    results = '\n'.join(result_list)
    with open(result_file, 'w') as f:
        f.write(results)
result_list='''
征服者CONQUEROR 更新 - 瑞憶科技有限公司Radareye Technologies ... ; http://www.radarway.com.tw/service1.php
[debug] 澳門廣播電視股份有限公司TDM-Teledifusão de Macau ; http://www.xihai.org/co/jump.php?id=3378
[debug] 【江苏核电有限公司2017校园招聘】江苏核电有限公司前程无忧官方校园 ... ; http://www.njsdmy.com/click.php?ID=7523&RedirectUrl=http%3A%2F%2Fcampus.51job.com%2Fcnnp
[debug] 公司简介 - 丰润泽 ; http://www.jzfrz.cn/about.php?id=1
[debug] 许达哲 简历资料新闻-中国党政领导干部资料库 ; http://gbzl.people.com.cn/grzy.php?id=121000575
[debug] 广汽本田官方网站-广汽本田让梦走得更远 ; http://www.autobaidu.com/urlAlter.php?url=http%3A%2F%2Fwww.ghac.cn%2F&id=514
[debug] 八、公司解散之意義為何？其原因(事由)有哪些？公司解散之效力為何 ... ; http://www.justlaw.com.tw/LRdetail.php?id=279
[debug] 台北港貨櫃碼頭股份有限公司 ; https://www.facebook.com/apps/application.php?id=170562592967724
[debug] Bamboo International Holding Co., Ltd. 竹福國際控股有限公司 ; http://www.bambooint.com.hk/chi/reference.php?id=15791
[debug] 關於我們 - Swissray Global ; http://www.swissray.com/menu.php?id=3
[debug] 广东因豪信息科技有限公司 ; http://www.cloudguide.com.cn/url.php?url=http://www.ksense.com/
[debug] 公司背景 - Gilman Group ; http://www.gilman-group.com/public/getitem.p
'''
result_list=result_list.strip().split('\n')
result_dir='keword-result-drive'
keywords='keywords.txt'
# print result_list
with open(keywords) as f:
	keywords=f.readlines()
	for keyword in keywords:
		keyword=keyword.strip().decode("utf-8")
		save_result_to_file(keyword,result_list,result_dir)