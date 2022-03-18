from django import template

from .. import models

register = template.Library()


@register.filter
def model_type(value):
    return type(value).__name__


@register.filter
def not_in_review(ticket):
    return not models.Review.objects.filter(ticket__exact=ticket).exists()
