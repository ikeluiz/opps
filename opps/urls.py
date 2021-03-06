#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from django.contrib import admin


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^redactor/', include('redactor.urls')),

    url(r'^sitemap', include('opps.sitemaps.urls')),
    url(r'^', include('opps.articles.urls', namespace='articles',
                      app_name='articles')),
)
