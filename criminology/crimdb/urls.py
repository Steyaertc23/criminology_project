from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('search/', search, name='search'),
    path('add-felon/', addFelon, name='addFelon'),
    path('add-misdomeanor/', addMisdomeanor, name='addMisdomeanor'),
    # path()
]