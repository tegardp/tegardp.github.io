#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tegardp'
SITENAME = "Tegar Dani's Blog"
SITEURL = 'https://tegardp.github.io'

PATH = 'content'
OUTPUT_PATH = '../output'
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['img', 'pdf']
PAGE_PATHS = ['pages']
THEME = 'theme/elegant'


TIMEZONE = 'Asia/Jayapura'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'