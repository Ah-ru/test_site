from django.urls import path
from .views import start, m3t

urlpatterns = [
    path('', start),
    path('s', m3t)
]