from django.urls import path
from mainapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_page, name='login'),
    path('register', views.register_page, name='register'),
    path('cds', views.cds, name='cds'),
    path('rock', views.rock, name='rock'),
    path('pop', views.pop, name='pop'),
    path('register_complete', views.register_complete, name='register_complete')
]
