from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .kafka_producer import send_message_to_kafka
# Create your views here.

@api_view(['POST'])
def send_to_kafka(request):
    message = request.data.get('message','Default message')
    send_message_to_kafka({'message':message})
    return Response({'status':'Message sent to Kafka'})
