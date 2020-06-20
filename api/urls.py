from django.urls import path, re_path
from .views import IndexAPIView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('api/v1/irrf/resultado', IndexAPIView.as_view(), name='api'),
]
