#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

from haystack.indexes import SearchIndex, CharField, DateTimeField
from haystack import site

from .models import Post


class PostIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    date_available = DateTimeField(model_attr='date_available')

    def get_updated_field(self):
        return 'date_available'

    def index_queryset(self):
        return Post.objects.filter(
            date_available__lte=datetime.datetime.now(),
            published=True)


site.register(Post, PostIndex)
