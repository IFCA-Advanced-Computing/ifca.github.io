#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'IFCA Advanced Computing and e-Science group'
SITENAME = u'IFCA Advanced Computing and e-Science group on GitHub'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Advanced Computing and e-Science group', 'https://computing.ifca.es'),
    ('Advanced Computing and e-Science group (wiki)', 'https://confluence.ifca.es'),
    ('Institute of Physics of Cantabria (IFCA)', 'https://ifca.unican.es'),
    ('Spanish National Research Council (CSIC)', 'https://www.csic.es'),
    ('University of Cantabria (UC)', 'https://www.unican.es/'),
)

DISPLAY_PAGES_ON_MENU = False

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/IFCA_Computing'),
          ('GitHub Profile', 'https://github.com/IFCA/'),)

DEFAULT_PAGINATION = False

THEME = "themes/sober"

PELICAN_SOBER_LOGO = "/images/logo.png"
PELICAN_SOBER_STICKY_SIDEBAR = True
PELICAN_SOBER_ABOUT = """We are part of a joint research center between the
Spanish National "Research Council (CSIC) and the University of Cantabria (UC),
providing 'enhanced' Science (or e-Science) services for science and research.
"""


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
