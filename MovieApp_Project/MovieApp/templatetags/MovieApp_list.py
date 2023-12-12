from django import template
from MovieApp.models import Movie, Category, MovieType
from MovieApp.utils import movie_filter
from django.db.models import Avg

register = template.Library()


@register.filter(name="type_wise_movie")
def type_wise_movie(request, movie_type):
    filter_string = movie_filter(request)
    return Movie.objects.filter(
        movie_type=movie_type, **filter_string
    )[:6].annotate(
        avg_rating=Avg('review__rating')
    )
