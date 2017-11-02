#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ivana Doležalová'
SITENAME = 'O Švédsku a tak'
SITETITLE = SITENAME
SITESUBTITLE = AUTHOR
SITEDESCRIPTION = 'Ivana Doležalová píše blog (nejen) o svém odchodu do Švédska'
SITEURL = 'http://ivadol.cz'
COPYRIGHT_YEAR = 2017
CC_LICENSE = {'name': 'CC BY-SA 3.0 CZ', 'link': 'https://creativecommons.org/licenses/by-sa/3.0/cz'}
SITELOGO = SITEURL + '/images/author.jpg'
FAVICON = SITEURL + '/images/favicon.ico'
PYGMENTS_STYLE = 'github'
BROWSER_COLOR = '#006AA8'
DISQUS_SITENAME = 'ivadol'

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'Europe/Prague'
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

SOCIAL = (('linkedin', 'https://www.linkedin.com/in/ivana-dolezalova'),
          ('github', 'https://github.com/akarienta'),
          ('stack-overflow', 'https://stackoverflow.com/users/3780766'))

MENUITEMS = (('Archiv', '/archives.html'),
             ('Kategorie', '/categories.html'),
             ('Tagy', '/tags.html'),)

DEFAULT_PAGINATION = 5

THEME = "themes/Flex"

MAIN_MENU = True
HIDE_FLEX_COPYRIGHT = True

PLUGIN_PATHS = ['plugins']
PLUGINS = ['post_stats', 'i18n_subsites']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
