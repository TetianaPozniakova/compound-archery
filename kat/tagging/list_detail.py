__author__ = 'noctule'

from django.views.generic.list import ListView


def object_list(request, **kwargs):
    kwargs.pop('template_object_name', None)
    return ListView.as_view(**kwargs)(request)
