from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

# for views 
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

"""
item 1:
login required decorators in  urls 
"""
class ProfileTemplateView(TemplateView):
    template_name = 'registration/profile.html'

class AboutTemplateView(TemplateView):
    template_name = 'registration/about.html'

"""
item 2:
login required decorators not in urls 
"""


class ProfileClassTemplateView(TemplateView):
    template_name = 'registration/profile.html'
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class AboutClassTemplateView(TemplateView):
    template_name = 'registration/about.html'
    @method_decorator(login_required)
    # @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

"""
item 3:
decorator in class 
"""
@method_decorator(login_required, name='dispatch')
class ProfileClassDecTemplateView(TemplateView):
    template_name = 'registration/profile.html'

@method_decorator(login_required, name='dispatch')
class AboutClassDecTemplateView(TemplateView):
    template_name = 'registration/about.html'