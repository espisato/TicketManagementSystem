from django.urls import path
from accounts.views import RegisterView,RequestView,LoginView,Homepage

urlpatterns = [
    path('homepage', Homepage.as_view(), name="homepage"),
    path('signup',RegisterView.as_view(),name='registration'),
    path('request',RequestView.as_view(),name='assign'),
    path('login/',LoginView.as_view(),name= 'user-login'),
]
