from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^posts$', views.post_list, name='post_list'),
    url(r'^posts/(?P<title>[\w ]+)', views.post),
    url(r'^$', views.post_list, name='post_list'),

    url(r'^writings$', views.writing_list, name='writing_list'),
    url(r'^writings/(?P<title>[\w ]+)', views.writing),
    url(r'^.*$', views.no_page_found),
]