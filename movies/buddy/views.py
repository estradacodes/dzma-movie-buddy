import requests
import urllib
import environ

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from .forms import LoginUserForm, RegisterUserForm
from .models import Movie

env = environ.Env()
environ.Env.read_env()

# Create your views here.
def index(request):
    search = 'harry potter'
    movies = getMovies(search)
    return render(request, 'index.html', {'movies': movies['results']})

def search(request):
    if request.method == 'POST':
        movies = getMovies(request.POST['query'])
        return render (request, 'index.html', {'movies': movies['results']})
    return redirect('home')

def buddy(request):
    user_list = getBuddyList(request)
    movie_list = getBuddyMovieDetails(user_list)
    context = {'movie_list': movie_list}
    return render(request, 'buddy.html', context)

def getBuddyMovieDetails(user_list):
    movie_list = []
    for movie in user_list:
        base_url='https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US'.format(movie.movie_id, env('API_KEY'))
        movie_list.append(requests.get(base_url).json())
    return movie_list

def movieDetails(request, movie_id):
    base_url='https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US'.format(movie_id, env('API_KEY'))
    movie_details = requests.get(base_url)
    trailer_url='https://api.themoviedb.org/3/movie/{}/videos?api_key={}&language=en-US'.format(movie_id, env('API_KEY'))
    trailer = requests.get(trailer_url)
    print(trailer_url)
    return render(request, 'movie.html', {'movie': movie_details.json(), 'trailer': trailer.json()})

def getMovies (search):
    base_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&language=en-US&query={}&page=1&include_adult=false'.format(env("API_KEY"), urllib.parse.quote(search))
    movie_list = requests.get(base_url)
    return movie_list.json()

# PROFILE

def logoutUser(request):
    logout(request)
    return redirect('buddy:index')

def loginUser(request):
    form = LoginUserForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('buddy:buddy')
    return render(request, 'login.html', {'form': form})

def registerUser(request):
    if request.user.is_authenticated:
        return redirect('buddy:buddy')
    else:
        if request.method == "POST":
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('buddy:buddy')
        form = RegisterUserForm()
        context = { 'form': form }
        return render(request, 'register.html', context) 

# USER MOVIE LIST 

def getBuddyList(request):
    movie_list = Movie.objects.filter(user=request.user)
    return movie_list

def deletefromList(request, movie_id):
    movie = Movie.objects.get(movie_id=movie_id)
    movie.delete()
    return redirect('buddy:buddy')


def addMovietoList(request, movie_id):
    Movie.objects.create(
        user = request.user,
        movie_id = movie_id
        )
    return redirect('buddy:buddy')