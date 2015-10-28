#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mack Stone'
SITENAME = u'Just A Page'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'cn'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Python.org', 'http://python.org/'),
         ('old blog', 'http://schi.iteye.com/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('weibo', 'http://weibo.com/mackst'),
          ('Github', 'https://github.com/mackst'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


#THEME = r'F:\coding\pelican-themes\bootstrap2-dark'
THEME = r'.\bootstrap2-dark'
CSS_FILE = "wide.css"

GITHUB_URL = 'https://github.com/mackst/mackst.github.io.git'