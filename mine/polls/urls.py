from django.conf.urls import url,include
from polls import views


app_name='polls'
urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^(?P<question_id>[0-9]+)/result/$',views.results,name='result'),
    url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),

]
