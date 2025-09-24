from django.urls import path
from . import views

app_name = "measurements"

urlpatterns = [
    path("", views.home, name="home"),
    path("scan/", views.scan_api, name="scan_api"),
    path("metrics/", views.metrics, name="metrics"),
]
