from django.urls import path
from .views import import SignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]