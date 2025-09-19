from django.urls import path, include

from rest_framework import routers
from cinema.views import ActorList, ActorDetail, GenreList, GenreDetail, CinemaHallViewSet, MovieViewSet

app_name = "cinema"

cinema_hall_list_view = CinemaHallViewSet.as_view(actions={'get': 'list', 'post': 'create'})
cinema_hall_detail_view = CinemaHallViewSet.as_view(actions={
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
router = routers.DefaultRouter()
router.register('movies', MovieViewSet, basename='movies')
router.register('cinema_halls', CinemaHallViewSet, basename='cinema_halls')

urlpatterns = [
    path('genres/', GenreList.as_view(), name='genre-list'),
    path('genres/<int:pk>/', GenreDetail.as_view(), name='genre-detail'),
    path('actors/', ActorList.as_view(), name="actor-list"),
    path('actors/<int:pk>/', ActorDetail.as_view(), name="actor-detail"),
    path('', include(router.urls)),
]
