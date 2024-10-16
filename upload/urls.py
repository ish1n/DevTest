from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),  # URL pattern for upload page
]
