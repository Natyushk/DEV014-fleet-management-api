from django.urls import path
from .views import HelloWorldView

urlpatterns = [
    path('taxi/', HelloWorldView.as_view(), name='hello-world'),
]