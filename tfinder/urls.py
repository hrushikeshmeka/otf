from django.urls import path

from . import views

urlpatterns = [
  path('',views.index, name = 'index'),
  path('home',views.home, name = 'home'),
  path('locator',views.locator, name = 'locator'), 
  path('register',views.register, name = 'register'),
  path('login',views.login, name = 'login'),
  path('logout',views.logout, name = 'logout'),
  path('tregister',views.tregister, name = 'tregister'),
  path('update',views.updatedata, name = 'updatedata'),
  path('post',views.post, name = 'post'),
  path('postv',views.postv, name = 'postv'),

  ]