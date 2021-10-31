
from django.urls import path

from .views import GetPutDeleteAPIView,PostAPIView

urlpatterns = [
    path('',PostAPIView.as_view()),
    path('<int:id>',GetPutDeleteAPIView.as_view()),
]
