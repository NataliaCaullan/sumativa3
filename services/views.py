from rest_framework import generics
from django.shortcuts import render
from .models import Service, Provider
from .serializers import ServiceSerializer

class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.filter(thru_date__isnull=True)
    serializer_class = ServiceSerializer

class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

def home(request):
    # Obtener los últimos servicios
    servicios_recientes = Service.objects.filter(thru_date__isnull=True)[:5]

    # Obtener información de todos los proveedores
    proveedores = Provider.objects.all()

    contexto = {
        'mensaje_bienvenida': '¡Bienvenido a la API-Inacap!',
        'servicios_recientes': servicios_recientes,
        'proveedores': proveedores,
    }

    return render(request, 'index.html', contexto)
