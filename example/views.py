# example/views.py
from datetime import datetime

from django.http import HttpResponse
from . import FetchDataFromBackEnd
#from . import FetchDataFromDB

def index(request):
    json_data = "null"
    if request.method == "GET":
        query_str = request.GET.get('query')
        if query_str == "STR_TYPE":
            search_str = request.GET.get('searchFor')
            json_data = FetchDataFromBackEnd.fetch_data_based_on_str_params(search_str=search_str.lower())
        elif query_str == "CAT_TYPE":
            search_str = request.GET.get('searchFor')
            json_data = FetchDataFromBackEnd.fetch_data_based_on_category_params(category=search_str)
        elif query_str == "PDT_TYPE":
            search_str = request.GET.get('searchFor')
            json_data = FetchDataFromBackEnd.fetch_data_based_on_product_params(product_id=search_str)
        #elif query_str == "LOGIN":
         #   user_name = request.GET.get('userName')
          #  password = request.GET.get('password')
           # json_data = FetchDataFromDB.validate_login_credentials_process_results(user_name, password)
        else:
            json_data = FetchDataFromBackEnd.fetch_data_based_on_query(query=query_str)
    return HttpResponse(json_data)
