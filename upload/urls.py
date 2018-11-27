# Blanca Martin and Luis Carabe pair number 10

# workflowrepository URL Configuration

from django.conf.urls import url
from upload import views as upload

urlpatterns = [
    url(r'^add_workflow/$', upload.add_workflow, name='add_workflow'),
]
