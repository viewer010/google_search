google_search
作用：
	利用python selenium模块来爬取google搜索结果，在源代码的基础上做了些修改
使用方法：
相关文件说明：

	google-web-search.py：从Google抓取某个关键词的所有结果，以“［debug］标题 ; 链接”显示，以一条链接一行的格式保存。
	google-web-search-state-crawler.py： 从Google抓取某个关键词的结果数，即提取类似“找到约 1,130,000 条结果”中的数字。＃没试过
	result-crawler.py： 从Google返回的结果链接中抓取文本。注意只会处理网页和pdf文件。（pdf的下载处理貌似有点问题，可能需要再改一下。）＃没试过

base_dir = os.path.dirname(__file__)＃获取当前路径
google_adds = 'google-add.txt'		＃为goolge的子域名，提供搜索，减少被google反爬虫限制次数
keywords = 'keywords.txt'			＃为google搜索关键词，例如 "公司inurl:php id"
keywords_remain = 'keywords_remain.txt'#core.py每运行一条关键词，就删掉重新写入该文件，猜测是用来断点保存用
useragents_text = 'useragent.txt'	＃随机变换useragent
result_dir = os.path.join(base_dir, 'keyword-result-drive')＃结果输出目录

来源：
	https://github.com/reee/Google-Web-Search-Crawler/
