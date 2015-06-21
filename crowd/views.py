from django.shortcuts import render
from sharepa import ShareSearch
import json
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def homepage(request):
    return render(request, 'homepage.html')

def ten(request):
    search = ShareSearch()
    first_ten = search.execute()
    return JsonResponse(first_ten.to_dict())

def getData(request):
	return HttpResponse(request, 'crowd/sharedata')
 
