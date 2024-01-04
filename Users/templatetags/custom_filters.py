
from django import template

register = template.Library()

@register.filter
def split_token(url):
    return url.split('/')[-3] + '/' + url.split('/')[-2]

####new change for email confirmation
@register.filter
def split_confirmation_token(url):
    return url.split('/')[-2]  


