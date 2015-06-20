from django.shortcuts import render
from sharepa import ShareSearch
import json
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def homepage(request):
    return render(request, 'homepage.html')

def ten(request):
    search = ShareSearch()
    first_ten = search.execute()
    return first_ten.to_dict()
 
