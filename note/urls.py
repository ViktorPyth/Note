from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/like/$', views.post_like, name='post_like'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^accounts/registration/$', views.register, name='registr'),
    url(r'^search-form/$', views.search_form , name='search_form'),
    url(r'^search/$', views.search, name='search' ),
    url(r'^sort_dataa/$', views.sort_dataa, name='sort_dataa'),
    url(r'^sort_alpha/$', views.sort_alpha, name='sort_alpha'),
    url(r'^sort_likea/$', views.sort_likea, name='sort_likea'),
]