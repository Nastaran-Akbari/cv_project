from .views import *
from django.urls import path

page_name = 'cv'

urlpatterns = [
    path('', index_view),
]