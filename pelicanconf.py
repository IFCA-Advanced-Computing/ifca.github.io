#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'IFCA'
SITENAME = u'grid.ifca.es'
SITEURL = ''

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/IFCA_Computing'),)

DEFAULT_PAGINATION = 10

DISPLAY_CATEGORIES_ON_MENU = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


THEME = "themes/ifca"

GITHUB_USER = "IFCA"
GITHUB_REPO_COUNT = 20

MENUITEMS = (
    ('Home', '/'),
    ('Blog', '/archives.html'),
    ('Wiki', 'http://grid.ifca.es/wiki'),
#    ('Support', '/support.html'),
)

ADDTHIS_PROFILE="xa-5257ddb854d1e8cd"
