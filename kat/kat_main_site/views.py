# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext


def main_page(request):
    return render_to_response('kat_main_page.html', RequestContext(request))