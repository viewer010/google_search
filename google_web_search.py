#!/usr/bin/env python2
# -*- coding: utf8 -*-

import os

from core import *

base_dir = os.path.dirname(__file__)
google_adds = 'google-add.txt'
keywords = 'keywords.txt'
keywords_remain = 'keywords_remain.txt'
useragents_text = 'useragent.txt'
result_dir = os.path.join(base_dir, 'keyword-result-drive')
if not os.path.exists(result_dir):
    os.makedirs(result_dir)

keywords_list = conv_to_list(keywords)
useragent_list = conv_to_list(useragents_text)
if keywords_list:
    crawl_all_keyword(keywords_list, keywords_remain, google_adds, useragent_list, result_dir)