# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import url
from service.views import IndexView

urlpatterns = [
    url('^$', IndexView.as_view(), name='index'),
]