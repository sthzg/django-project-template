# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.utils.translation import ugettext_lazy as _
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from service.apiserializers import IndexSerializer


@api_view(('GET',))
def api_root(request, format=None):
    """ Provides a root view for the browsable api. """
    return Response({
        'index': reverse('service-api:index', request=request, format=format)
    })


class IndexApiView(APIView):
    """ Provides a Hello World endpoint to be overridden or trashed. """
    def get(self, request):
        content = {'greeting': "Hello World"}
        serializer = IndexSerializer(content)
        return Response(serializer.data)
