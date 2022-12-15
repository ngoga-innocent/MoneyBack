from django.urls import path
from . import views

urlpatterns = [

    path('', views.Register),
    path('login', views.Login),
    path('logout', views.logout),
    path('account', views.account)
]
