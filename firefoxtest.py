#coding=utf-8
from selenium import webdriver

driver=webdriver.Firefox()
url='http://ip.cn'
driver.get(url)
e=driver.find_element_by_class_name('well')
for i in e.find_elements_by_tag_name('code'):
	print i.text
