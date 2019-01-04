# from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import url
from storageapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    url('admin/', admin.site.urls),
]

urlpatterns += [
    url('^$', views.main),
    url(r'^file/', include('storageapp.urls')),
]


