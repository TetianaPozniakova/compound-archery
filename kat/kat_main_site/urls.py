__author__ = 'noctule'
from django.conf.urls import patterns
from django.views.generic import TemplateView
from kat_main_site.views import main_page


urlpatterns = patterns('',
    (r'^$', main_page),

    # Static pages
    (r'^contacts/', TemplateView.as_view(template_name="contacts_page.html")),

)