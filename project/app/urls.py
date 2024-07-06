from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework import routers 
from .views import *
  

router = routers.DefaultRouter()
router.register(r'movie', MovieViewSet, basename='movie')
router.register(r'student', StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]