from django.conf.urls import url
from . import views

app_name = 'soccerApp'

urlpatterns = [
    
    # index 
    url(r'^$',views.IndexView.as_view(),name='index'),
    
    #/statics
    url(r'^statics$',views.StaticsView.as_view(),name='statics'),


    #/team/12
    url(r'^team/(?P<pk>[0-9]+)/$',views.DetailsView.as_view(),name='details'),


]
