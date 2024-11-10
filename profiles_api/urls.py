from django.urls import path, include
from profiles_api import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

"""
need to specify base_name parameter for viewset that doesn't have a queryset
or if we want to override the name of the queryset
"""
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]