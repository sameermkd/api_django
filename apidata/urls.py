from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("data/<int:id>", views.data, name="data")
]