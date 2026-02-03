from django.shortcuts import render
from rest_framework import viewsets
from .models import Greeting
from .serializers import GreetingSerializer

def home(request):
    return render(request, 'index.html')  # Plain Django view - returns HTML, not JSON

class GreetingViewSet(viewsets.ModelViewSet):
    queryset = Greeting.objects.all()
    serializer_class = GreetingSerializer