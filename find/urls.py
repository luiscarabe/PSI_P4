# Blanca Martin and Luis Carabe pair number 10

# workflowrepository URL Configuration

from django.conf.urls import url
from find import views


# All urls for workflow lists/search/detail
urlpatterns = [
    url(r'^$', views.workflow_list, name='workflow_list'),
    url(r'^workflow_list/(?P<category_slug>[-\w]+)/$', views.workflow_list, name='workflow_list_by_category'),
    url(r'^workflow_detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.workflow_detail, name='workflow_detail'),
    url(r'^workflow_search/(?P<name>[-\w]+)/$', views.workflow_search, name='workflow_search'),
    url(r'^workflow_search/$', views.workflow_search, name='workflow_search'),
    url(r'^workflow_download/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.workflow_download, name='workflow_download'),
    url(r'^workflow_download_json/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.workflow_download_json, name='workflow_download_json'),
]