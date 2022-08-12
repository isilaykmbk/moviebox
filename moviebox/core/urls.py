from django.urls import path

from moviebox.core.views import index, DashboardView, MovieDetails, ViewAllRating, ViewAllPopular, \
    SearchView , GenreView

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', DashboardView.as_view(), name='home'),
    path('search-result/', SearchView.as_view(), name='search_result'),
    path('movie-details/<str:id>', MovieDetails.as_view(), name='details'),
    path('view-all-rating/<str:page>', ViewAllRating.as_view(), name='view_all_rating'),
    path('view-all-popular/<str:page>', ViewAllPopular.as_view(), name='view_all_popular'),
    path('genre/<str:category>/', GenreView.as_view(), name='genre'),

]
