# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.shortcuts import render
from django.views.generic.base import View


class IndexView(View):
    def get(self, request):
        return render(
            request,
            'service/base.html',
            {}
        )
