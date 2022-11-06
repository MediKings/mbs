from django.urls import path
from .views import (Home, Single, Play
# DetailPost, Films, Series, Genres
)

app_name='home'

urlpatterns = [
    path('', Home, name='home'),
    path('single/<str:slug>/', Single, name='single'),
    path('play/<str:slug>/', Play, name='play'),
    # path('search/', Search, name='search'),
]