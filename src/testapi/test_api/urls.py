from django.urls import path

from . import views
from django.conf.urls import url

urlpatterns = [
    path('hello/',views.HelloApiView.as_view()),
]