from django.shortcuts import render
from django.http import HttpResponse
from .Forms import SubscriberForm

# Create your views here.


def landing(request):

    form = SubscriberForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        new_form = form.save()
    return render(request, 'landing.html', locals())


def order():
    return 1


def product():
    return 1
