# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from rest_framework import serializers


class IndexSerializer(serializers.Serializer):
    greeting = serializers.CharField(max_length=100)
