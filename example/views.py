# example/views.py
from datetime import datetime

from django.http import HttpResponse
from . import FetchDataFromBackEnd


def index(request):
    json_data = "null"
    if request.method == "GET":
        query_str = request.GET.get('query')
        print("a: ", query_str)
        json_data = FetchDataFromBackEnd.fetch_data_based_on_query(query=query_str)
    return HttpResponse(json_data)