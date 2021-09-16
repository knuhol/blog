#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Knut Holm'
SITENAME = 'O Švédsku a tak'
SITETITLE = SITENAME
SITESUBTITLE = AUTHOR
SITEDESCRIPTION = 'Knut Holm píše blog (nejen) o svém odchodu do Švédska'
SITEURL = 'https://svedsko.blog'
COPYRIGHT_YEAR = '2017-2021'
CC_LICENSE = {'name': 'CC BY-SA 4.0', 'link': 'https://creativecommons.org/licenses/by-sa/4.0/deed.cs'}
SITELOGO = SITEURL + '/images/author.jpg'
OG_IMAGE = SITEURL + '/images/og.png'
FAVICON = SITEURL + '/images/favicon.ico'
PYGMENTS_STYLE = 'github'
BROWSER_COLOR = '#006AA8'
DISQUS_SITENAME = 'ivadol'
GOOGLE_ANALYTICS = 'UA-110306205-1'

PATH = 'content'
STATIC_PATHS = ['images', 'files']

TIMEZONE = 'Europe/Stockholm'
DEFAULT_DATE_FORMAT = '%-d. %-m. %Y (%-H:%M)'

I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'cs'
OG_LOCALE = 'cs_CZ'
LOCALE = 'cs_CZ'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SOCIAL = (('linkedin', 'https://www.linkedin.com/in/knuhol'),
          ('github', 'https://github.com/knuhol'),
          ('stack-overflow', 'https://stackoverflow.com/users/3780766'))

MENUITEMS = (('Archiv', '/archives.html'),
             ('Kategorie', '/categories.html'),
             ('Tagy', '/tags.html'),
             ('Autoři', '/authors.html'))

DEFAULT_PAGINATION = 5

THEME = "themes/Flex"

MAIN_MENU = True
HIDE_FLEX_COPYRIGHT = True
MORE_AUTHORS = True

PLUGIN_PATHS = ['plugins']
PLUGINS = ['post_stats', 'i18n_subsites']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
