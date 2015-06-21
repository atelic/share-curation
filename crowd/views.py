from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
import itertools

from sharepa import ShareSearch, bucket_to_dataframe
from elasticsearch_dsl import F, Q


# Create your views here.
def index(request):
    return render(request, 'index.html')

def homepage(request):
    return render(request, 'homepage.html')

def ten(request):
    my_results = _make_empty_query()
    return JsonResponse(my_results, safe=False)

def _make_empty_query(beginning_index=0, end_index=10):
    from elasticsearch_dsl import F, Q

    my_search = ShareSearch()
    my_search = my_search.query(
    'query_string', # Type of query, will accept a lucene query string
    query='NOT description:* OR NOT uri:* OR NOT publisher:* OR NOT doi:* OR NOT sponsorships:* OR NOT licenses:* OR NOT languages:*',
    analyze_wildcard=True  # This will make elasticsearch pay attention to the asterisk (which matches anything)
    )
    ret = my_search[beginning_index:end_index].execute()
    return ret.to_dict()

def slice_and_dice(jsonBlob):
    new_data = dict()
    count = 0
    for item in jsonBlob:
        new_data['item {}'.format(count)] = jsonBlob[count]
        count += 1

    return new_data

    
    for item in jsonBlob['hits']['hits']:
        item = item.to_dict()
        new_item = {
            'title': item['source']['title'],
            'description': item['source']['description'],
            'contributors': item['source']['contributors'],
        }
        new_data['item {}'.format(count)] = new_item
        count += 1

    return new_data


def _post_to_share(json_schema):
    import urllib2, base64

    request = urllib2.Request("http://staging.osf.io/api/v1/share/data")
    base64string = base64.encodestring('%s:%s' % (eric, eric)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)   
    result = urllib2.urlopen(request)
