from django.shortcuts import render
from app1.models import random

# Create your views here.


def index(req):
    if req.method == 'GET':
        quotes = req.POST.get('quotes')
        author = req.POST.get('name')
        random.objects.create(quotes=quotes, author=author)
    return render(req, 'index.html')
