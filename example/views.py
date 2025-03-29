# example/views.py
from datetime import datetime

from django.http import HttpResponse
from . import FetchDataFromBackEnd
from . import FetchDataFromDB


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
        elif query_str == "LOGIN":
            user_name = request.GET.get('userName')
            password = request.GET.get('password')
            json_data = FetchDataFromDB.validate_login_credentials_process_results(user_name, password)
        elif query_str == "SAVE_LEADS":
            module= request.GET.get('module')
            Name= request.GET.get('Name')
            Email= request.GET.get('Email')
            Message = request.GET.get('Message')
            if module == "leads_form":
                Country= request.GET.get('Country')
                PhoneNumber= request.GET.get('PhoneNumber')
                CompanyName= request.GET.get('CompanyName')
                interestedIn= request.GET.get('interestedIn')
                json_data = FetchDataFromDB.save_leads_from_website(module=module,
                                                                    Name=Name,
                                                                    Email=Email,
                                                                    Country=Country,
                                                                    PhoneNumber=PhoneNumber,
                                                                    CompanyName=CompanyName,
                                                                    interestedIn=interestedIn,
                                                                    Message=Message)
            elif module == "message":
                json_data = FetchDataFromDB.save_message_from_website(module=module,
                                                                    Name=Name,
                                                                    Email=Email,
                                                                    Message=Message)
        else:
            json_data = FetchDataFromBackEnd.fetch_data_based_on_query(query=query_str)
    else:
        query_str = request.GET.get('query')
        json_data = FetchDataFromBackEnd.fetch_data_based_on_query(query=query_str)

    return HttpResponse(json_data)
#   timestamp,
#   module #leads_form or message
#   Name
#   Email
#   Country
#   PhoneNumber
#   CompanyName
#   interestedIn
#   leads_Message
#   read



# timestamp: new Date(Date.now()), module: "leads_form", Name: "tester", Email: "tester@admin.com" , Country: "India", PhoneNumber: "9168669610", CompanyName: "Saharsh Bhadani Venture Private Limited", interestedIn: "Data Analytics", leads_Message: "some really big message", read: "0"