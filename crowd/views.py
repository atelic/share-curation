from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

from sharepa import ShareSearch, bucket_to_dataframe
from elasticsearch_dsl import F, Q


# Create your views here.
def index(request):
    return render(request, 'index.html')

def homepage(request):
    return render(request, 'homepage.html')

def ten(request):
    my_results = _make_empty_query()
    return JsonResponse(my_results.to_dict())

def _make_empty_query(beginning_index=0, end_index=10):
    from elasticsearch_dsl import F, Q

    my_search = ShareSearch()
    my_search = my_search.query(
    'query_string', # Type of query, will accept a lucene query string
    query='NOT description:* OR NOT uri:* OR NOT publisher:* OR NOT doi:* OR NOT sponsorships:* OR NOT licenses:* OR NOT languages:*',
    analyze_wildcard=True  # This will make elasticsearch pay attention to the asterisk (which matches anything)
    )

    return my_search[beginning_index:end_index].execute()
