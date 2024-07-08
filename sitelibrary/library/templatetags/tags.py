from django import template
from library import views

register = template.Library()


@register.simple_tag()
def get_genres():
    return views.list_genre


@register.simple_tag()
def get_menu():
    return views.menu


@register.simple_tag()
def get_authors():
    return views.get_authors()


@register.simple_tag()
def get_books():
    return views.books
