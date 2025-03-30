import pymongo
from bson.objectid import ObjectId
import pandas as pd
from datetime import datetime
from . import TableDetails


def get_connection():
    uri = TableDetails.DATA_BASE_URL
    my_client = pymongo.MongoClient(uri)
    # print(my_client)
    return my_client


def use_database(my_client):
    db = my_client[TableDetails.DATE_BASE_NAME]
    return db


def get_collection_from_database(db, table_name):
    return db[table_name]


def get_results_for_user_name(table, user_name, password):
    result = table.find_one({TableDetails.USER_TABLE["USER_EMAIL"] : user_name.lower(), TableDetails.USER_TABLE["USER_PASSWORD"] : password})
    if result is None:
        return None
    else:
        df = pd.json_normalize(result)
        return df


def validate_login_credentials_process_results(user_name, password):
    my_client = get_connection()
    db = use_database(my_client)
    table = get_collection_from_database(db, "USER_TABLE")
    result = get_results_for_user_name(table, user_name, password)
    if result is None:
        return '[{"userID": "invalid", "userType": "invalid"}]'
    else:
        return convert_data_frame_to_json(result[['userID', 'userType']])


def save_leads_from_website(module= "leads_form",
                            Name= "Tester Kumar",
                            Email= "tester@admin.com" ,
                            Country= "India",
                            PhoneNumber= "9168669610",
                            CompanyName= "Saharsh Bhadani Venture Private Limited",
                            interestedIn= "Data Analytics",
                            Message= "some really big message",
                            ):
    timestamp = datetime.utcnow()
    my_client = get_connection()
    db = use_database(my_client)
    table = get_collection_from_database(db, "leads")
    result = save_results_in_leads_table(table=table,
                                         timestamp=timestamp,
                                         module=module,
                                         Name=Name,
                                         Email=Email,
                                         Country=Country,
                                         PhoneNumber=PhoneNumber,
                                         CompanyName=CompanyName,
                                         interestedIn=interestedIn,
                                         Message=Message)
    if result is None:
        return '[{"inserted_id": "invalid"}]'
    else:
        return '<!DOCTYPE html><html><body><p>Data Saved Successfully.</p></body></html>'


def save_results_in_leads_table(table,
                                timestamp,
                                module= "leads_form",
                                Name= "Tester Kumar",
                                Email= "tester@admin.com" ,
                                Country= "India",
                                PhoneNumber= "9168669610",
                                CompanyName= "Saharsh Bhadani Venture Private Limited",
                                interestedIn= "Data Analytics",
                                Message= "some really big message",
                                read= "0"
                                ):
    result = table.insert_one(
        {
            TableDetails.leads["leads_timestamp"]: timestamp,
            TableDetails.leads["leads_module"]: module,
            TableDetails.leads["leads_name"]: Name,
            TableDetails.leads["leads_email"]: Email,
            TableDetails.leads["leads_Country"]: Country,
            TableDetails.leads["leads_PhoneNumber"]: PhoneNumber,
            TableDetails.leads["leads_CompanyName"]: CompanyName,
            TableDetails.leads["leads_interestedIn"]: interestedIn,
            TableDetails.leads["leads_Message"]: Message,
            TableDetails.leads["leads_read"]: read
        }
    )
    return result


def save_message_from_website(module="Message",
                              Name="Tester Kumar",
                              Email="tester@admin.com",
                              Message="some really big message",
                              read="0"
                            ):
    timestamp = datetime.utcnow()
    my_client = get_connection()
    db = use_database(my_client)
    table = get_collection_from_database(db, "leads")
    result = save_results_in_leads_table(table=table,
                                         timestamp=timestamp,
                                         module=module,
                                         Name=Name,
                                         Email=Email,
                                         Message=Message,
                                         read=read)
    if result is None:
        return '[{"inserted_id": "invalid"}]'
    else:
        return '[{"inserted_id":'+str(result.inserted_id)+'}]'


def fetch_all_leads_and_messages_from_leads_table():
    my_client = get_connection()
    db = use_database(my_client)
    table = get_collection_from_database(db, "leads")
    result = get_all_data_from_leads_table(table)
    return convert_data_frame_to_json(result)


def get_all_data_from_leads_table(table):
    result = table.find()
    if result is None:
        return "[]"
    else:
        df = pd.json_normalize(result)
        # Convert to datetime
        df["timestamp"] = pd.to_datetime(df["timestamp"], format="%Y-%m-%d %H:%H:%S")

        # Set date as index
        df = df.set_index("timestamp")

        return df[['timestamp', 'module', 'Name', 'Email', 'Country', 'PhoneNumber', 'CompanyName',
        'interestedIn', 'Message', 'read']]


def save_new_leads_for_future(timestamp):
    pass


def discard_new_leads_now(timestamp):
    pass


def discard_message_now(timestamp):
    pass


def discard_saved_leads_now(timestamp):
    pass


def convert_data_frame_to_json(df):
    json_str = df.to_json(orient="records")
    return json_str


if __name__ == '__main__':
    pass
    #print(fetch_all_leads_and_messages_from_leads_table())