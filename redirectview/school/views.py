from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
# Create your views here.

class RonaldoRedirectView(RedirectView):
    url = 'https://www.google.com'

class MbappeRedirectView(RedirectView):
    # when the url is hit, it should find the pattern_name and hit the url with this pattern name
    pattern_name = 'mindex' 
    permanent = True # status code changed from 302 to 301
    query_string = True  # when this is done the query will remain on the url for example url 127.0.0.1:8000/roll/12/?isdcjhdshfckh
    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        kwargs['pk'] = 16
        return super().get_redirect_url(self, *args, **kwargs)


