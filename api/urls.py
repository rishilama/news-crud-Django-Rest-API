from django.urls import path
from django.urls.conf import include
from rest_framework import routers 
from . import views

router = routers.DefaultRouter()
router.register('news', views.NewsViewSets, basename='news')

urlpatterns = [
    path('', include(router.urls))
]
