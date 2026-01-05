# from django.urls import path
# from .views import StudentRetrievUpdateDeleteAPI, StudentListCreateAPI


# urlpatterns = [
#     path('students/', StudentListCreateAPI.as_view()),
#     path('students/<int:pk>/', StudentRetrievUpdateDeleteAPI.as_view()),
    

# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register('students', StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls))
]
