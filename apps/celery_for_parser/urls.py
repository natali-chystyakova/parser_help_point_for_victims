from django.urls import path

from . import views

app_name = "celery_for_parser"

urlpatterns = [
    path("", views.CeleryView.as_view(), name="index"),
]
