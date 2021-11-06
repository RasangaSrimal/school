from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('gallery', views.gallery, name='gallery'),
    path('events', views.events, name='events'),
    path('news', views.news, name='news'),
    path('identity', views.identity, name='identity'),
    path('history/', views.history, name='history'),
    path('academic/', views.academic, name='academic'),
    path('achievements/', views.achievements, name='achievements'),
]
