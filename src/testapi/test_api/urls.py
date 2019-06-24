from django.urls import path,include

from . import views
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('APIViewset', views.HelloViewsets, base_name= 'Viewset')
router.register('profile', views.UserProfileViewset)
router.register('login', views.LoginViewSet, base_name='Login')
router.register('feed', views.UserProfileFeedViewSet)


urlpatterns = [
    path('hello/',views.HelloApiView.as_view()),
    path('',include(router.urls))
]