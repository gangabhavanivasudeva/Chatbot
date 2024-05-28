from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('chatbot', views.index, name='index'),
    path('admission', views.GetCollegeAdd, name='GetCollegeAdd'),
    path('placements', views.GetCollegePlacements, name='GetCollegePlacements'),
    path('infra', views.getInfra, name='getInfra'),
    path('hostel', views.getHostelfees, name='getHostelfees'),
    path('env', views.getcolEnv, name='getcolEnv'),
    path('achievements', views.getcolach, name='getcolach'),
    path('naac', views.getcolnaac, name='getcolnaac'),
    path('nirf', views.getcolnirf, name='getcolnirf'),
    path('sendReminder', views.sendReminder, name='sendReminder'),
    path('setReminder', views.setReminder, name='setReminder'),
    path('logout', views.lgt, name='logout'),
]