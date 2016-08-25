from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^posts/(?P<title>[\w ]+)', views.post),
    url(r'^.*$', views.no_page_found),
    #url(r'^/post/(?P<title>\w{0,50})$', views.post),
]