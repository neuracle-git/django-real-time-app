from django.urls import path
from .views import send_to_kafka

urlpatterns = [
    path('send-kafka/', send_to_kafka, name='send_to_kafka'),
]
