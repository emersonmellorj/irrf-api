from django.urls import path
from .views import IndexAPIView

urlpatterns = [
    path('api/v1/irfp/', IndexAPIView.as_view(), name='index'),
]
