from django.urls import path
from .views import AddSerie

app_name='back'

urlpatterns = [
    path('add/serie/', AddSerie.as_view(), name='add-serie'),
]