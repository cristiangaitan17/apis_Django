from django.urls import path
from .views import RutinaListView

urlpatterns = [
    path('rutinas/', RutinaListView.as_view(), name='rutinas-list'),
]