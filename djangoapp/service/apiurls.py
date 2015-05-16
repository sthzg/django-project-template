# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _
from service import apiviews


urlpatterns = [
    url(r'^$', apiviews.api_root),
    url(r'^index/$', apiviews.IndexApiView.as_view(), name='index'),
]
