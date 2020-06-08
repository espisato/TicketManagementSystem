from django.urls import path
<<<<<<< HEAD
from accounts.views import RegisterView,RequestView,LoginView,Homepage

urlpatterns = [
    path('homepage', Homepage.as_view(), name="homepage"),
    path('signup',RegisterView.as_view(),name='registration'),
    path('request',RequestView.as_view(),name='assign'),
    path('login/',LoginView.as_view(),name= 'user-login'),
=======
from . import views

urlpatterns = [
    path('', views.index, name="index"),
>>>>>>> de971c457c57b32399128ec0900d27bd168bb331
]
