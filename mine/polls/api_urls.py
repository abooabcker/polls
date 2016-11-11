from django.conf.urls import url,include
from rest_framework import routers
from polls import drfview


router = routers.DefaultRouter()
#router.register(r'questions',drfview.QuestionView)
router.register(r'stat',drfview.StatView)



app_name='polls'
urlpatterns = [
    #url(r'^',include(router.urls)),
    url(r'^questions/$',drfview.QuestionView.as_view({'get':'list','post':'create'}),name='question_list'),
    url(r'^questions/(?P<pk>[0-9]+)/$',drfview.QuestionView.as_view({'delete':'change_status','patch':'partial_update'}),name='qestion_details'),
    url(r'^random/$',drfview.RandomView.as_view(),name='random_view'),
    url(r'^',include(router.urls))
    
]
