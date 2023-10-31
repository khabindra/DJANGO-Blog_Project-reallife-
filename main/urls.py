from django.urls import path
from . import views
urlpatterns = [
     path('',views.home,name="home"),
     path('mail/',views.send_email,name='send_email'),
     path('register/',views.user_registration,name='register'),
     path('login/',views.login_form,name='login_form'),
     path('logout/',views.logout_form,name='logout')
]
