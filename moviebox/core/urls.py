from django.urls import path

from moviebox.core.views import index, DashboardView, MovieDetails, ViewAllUpcoming, ViewAllRating, ViewAllPopular

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', DashboardView.as_view(), name='home'),
    path('movie-details/<str:id>', MovieDetails.as_view(), name='details'),
    path('view-all-upcoming/', ViewAllUpcoming.as_view(), name='view_all_upcoming'),
    path('view-all-rating/<str:page>', ViewAllRating.as_view(), name='view_all_rating'),
    path('view-all-popular/<str:page>', ViewAllPopular.as_view(), name='view_all_popular'),
]