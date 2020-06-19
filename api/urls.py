from django.urls import path
from .views import IndexAPIView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('api/v1/irfp/', IndexAPIView.as_view(), name='api'),
]
