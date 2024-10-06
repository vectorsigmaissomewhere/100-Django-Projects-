from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/', views.myview, name='func'), # url for function based view
    path('cl/', views.MyView.as_view(), name='cl'), # url for class based view
    # path('cl/', views.MyView.as_view(name='Ronaldo'), name='cl') # pass value in views  
    path('subcl/', views.MyViewChild.as_view(), name='subcl'),
    path('homefun/', views.homefun, name='homefun'),
    path('homecl/', views.HomeClassView.as_view(), name='homecl'),
    path('aboutfun/', views.aboutfun, name='aboutfun'),
    path('aboutcl/', views.AboutClassView.as_view(), name='aboutcl'),
    path('contactfun/', views.contactfun, name='contactfun'),
    path('contactcl/', views.ContactClassView.as_view(), name='contactcl'),
    path('newsfun/', views.newsfun, name='newsfun'),
    #path('newscl/', views.NewsClassView.as_view(), name='newscl'), # don't send the template
    path('newscl/', views.NewsClassView.as_view(template_name='school/news.html'), name='newcl'), # send the template from views
]
