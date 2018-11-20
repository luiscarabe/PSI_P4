# Blanca Martin and Luis Carabe pair number 10

# workflowrepository URL Configuration

from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from data import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^base/', views.base, name='base'),
    url(r'', include('find.urls')), # Include of urls defined in our app find
    url(r'', include('upload.urls')), # Include of urls defined in our app upload

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
