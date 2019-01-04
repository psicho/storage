from django.conf.urls import url
from storageapp import views

urlpatterns = [
   url(r'^upload/(.+)$', views.upload, name='upload'),
   url(r'^upload/(.?)$', views.upload, name='upload-main'),
   url(r'^download/(.+)$', views.download, name='download'),
   url(r'^delete/(.+)$', views.delete, name='delete'),

]
