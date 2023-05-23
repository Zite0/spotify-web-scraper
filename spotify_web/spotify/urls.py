from django.urls import path

from spotify import views

app_name = 'spotify'
urlpatterns = [
    path('', views.index, name='index'),
    path('404', views.error404, name='404'),
]