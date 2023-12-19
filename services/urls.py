from django.urls import path
from .views import ServiceList, ServiceDetail

urlpatterns = [
    path('services/', ServiceList.as_view(), name='service-list'),
    path('services/<int:pk>/', ServiceDetail.as_view(), name='service-detail'),
]
