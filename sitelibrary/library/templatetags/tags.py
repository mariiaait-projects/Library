from datetime import datetime

from django import template
from library import views
from library.models import Genre

register = template.Library()


@register.simple_tag()
def get_genres():
    return Genre.objects.all()


@register.simple_tag()
def get_menu():
    return views.menu

@register.simple_tag()
def get_manage_menu():
    return views.manage_menu


@register.simple_tag()
def get_authors():
    return views.get_authors()


@register.simple_tag()
def get_books():
    return views.books

@register.simple_tag()
def get_year():
    return datetime.now().year


