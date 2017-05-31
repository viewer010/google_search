#google_search
##作用：
	利用python selenium模块来爬取google搜索结果，在源代码的基础上做了些修改

##相关文件说明：
	
 - google-web-search.py：从Google抓取某个关键词的所有结果，以“［debug］标题 ; 链接”显示，以一条链接一行的格式保存。
 - google-web-search-state-crawler.py： 从Google抓取某个关键词的结果数，即提取类似“找到约 1,130,000 条结果”中的数字。＃没试过
 - result-crawler.py： 	从Google返回的结果链接中抓取文本。注意只会处理网页和pdf文件。（pdf的下载处理貌似有点问题，可能需要再改一下。）＃没试过

##使用方法：
```
	#使用python2 + selenium + firefox profile 实现的随机user agent 模拟抓取Google搜索结果和关键词的结果数。
	#首先请自行安装selenium
	cd google_search
	python google_web_search.py
	#程序会在当前目录下创建一个keyword-result-drive目录，里面以每条google搜索关键词为文件名的txt文件，文件内容为搜索结果
	#在console输出端，以“［debug］标题 ; 链接”显示爬取结果
```
配置说明:
```
base_dir = os.path.dirname(__file__)＃获取当前路径
google_adds = 'google-add.txt'		＃为goolge的子域名，提供搜索，减少被google反爬虫限制次数
keywords = 'keywords.txt'			＃为google搜索关键词，例如 "公司inurl:php id"
keywords_remain = 'keywords_remain.txt'#core.py每运行一条关键词，就删掉重新写入该文件，猜测是用来断点保存用
useragents_text = 'useragent.txt'	＃随机变换useragent
result_dir = os.path.join(base_dir, 'keyword-result-drive')＃结果输出目录
```

参考来源：
	https://github.com/reee/Google-Web-Search-Crawler/
