from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^log/(?P<pseudo>\w+)/$', views.index_log, name='index_log'),
    url(r'^log/(?P<pseudo>\w+)/send/$', views.send, name='send'),
    url(r'^log/(?P<pseudo>\w+)/delete/(?P<notice_id>\d+)/$', views.delete, name='delete'),
    url(r'^log/(?P<pseudo>\w+)/change_notice/(?P<notice_id>\d+)/$', views.change_notice, name='change_notice'),
    url(r'^log/(?P<pseudo>\w+)/change_now/(?P<notice_id>\d+)/$', views.change_now, name='change_now'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login/try/$', views.login_try, name='login_try'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/try/$', views.register_try, name='register_try'),
]
