from django.urls import path
from blog_app import views

urlpatterns = [
    path('',views.singup, name='singup'),
    path('login/',views.login, name='login'),
    path('home/',views.home, name='home'),
    path('web_development/',views.web_development, name='web_development'),
    path('blockchain_technology/',views.blockchain_technology, name='blockchain_technology'),
    path('cryptocurrency/',views.cryptocurrency, name='cryptocurrency'),
]
