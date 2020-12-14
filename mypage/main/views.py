from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.

def index(response):
    return HttpResponse("<h1>Pylyv's on Zero Day Code</h1>")

def from_database(response, id):
    ls = ToDoList.objects.get(id=id)
    return HttpResponse(f"<h1>{ls.name}</h1>")
