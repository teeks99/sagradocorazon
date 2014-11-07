#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Thomas Kent'
SITENAME = u'Sagrado Coraz\xf3n'
SITEURL = ''

TIMEZONE = 'America/La Paz'

DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
	('Principal', '/'),
	('Centro', '/pages/centro-pastoral.html'),
        ('Instituto', '/pages/instituto-san-jose-sebastian-pelczar.html'),
        ('Guarderia', '/pages/guarderia-san-antonio.html'),
        ('Kinder', '/pages/kinder-san-antonio.html'),
        ('Hogar', '/pages/hogar-sagrado-corazon.html'),
        ('Hermanas', '/pages/los-hermanas-en-bolivia.html'))
