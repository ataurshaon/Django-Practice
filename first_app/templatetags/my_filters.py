from django import template

register = template.Library()

def my_filter(value):
    return value + " This is custom filter "

register.filter('custom_filter', my_filter)