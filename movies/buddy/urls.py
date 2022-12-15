from django.urls import path, include

from . import views

app_name="buddy"
urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.search, name="search"),
    path('buddy/', views.buddy, name="buddy"),
    path('logout/', views.logoutUser, name="logout"),
    path('login/', views.loginUser, name="login"),
    path('register/', views.registerUser, name="register"),

    path('movie/<int:movie_id>/', views.movieDetails, name="movie"),
    path('movie/add/<int:movie_id>/', views.addMovietoList, name='addMovie'),
    path('movie/delete/<int:movie_id>/', views.deletefromList, name='deleteMovie'),

]
