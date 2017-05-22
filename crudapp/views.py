from django.shortcuts import render
from django.http import HttpResponse
from models import Books
# Create your views here.

def index(request):
    books = Books.

    return render(request,'index.html', {
        'books' : books
    })