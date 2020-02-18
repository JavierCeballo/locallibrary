from django.conf.urls import url

from . import views

# Loquqe sea 
urlpatterns = [
    url(r'^$', views.index, name='index'),
]



