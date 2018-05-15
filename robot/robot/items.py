# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from web.models import WebInfo,Keywords
class RobotItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = WebInfo

class KeywordsItem(DjangoItem):
    django_model = Keywords

