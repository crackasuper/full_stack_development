from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name= 'home'),
    path("contact", views.contact, name='contact'),
    path("about", views.about, name = 'about'),
    path("search", views.search, name='search'),
    path('signup', views.signup, name= 'signup'),
    path('login', views.login,name='login'),
    path('log_out', views.log_out, name='log_out')

]