from django.urls import path,include

from . import views
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('APIViewset', views.HelloViewsets, base_name= 'Viewset')
router.register('profile', views.UserProfileViewset)

urlpatterns = [
    path('hello/',views.HelloApiView.as_view()),
    path('',include(router.urls))
]