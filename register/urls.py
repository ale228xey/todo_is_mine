from django.urls import path, include

from register.views import UserRegistrationView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
]
