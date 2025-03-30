import pymongo
from bson.objectid import ObjectId
import pandas as pd
from datetime import datetime, timedelta
import time
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
    result = table.find().sort({TableDetails.leads["leads_timestamp"]: 1})
    if result is None:
        return "[]"
    else:
        df = pd.json_normalize(result)

        return df[['timestamp', 'module', 'Name', 'Email', 'Country', 'PhoneNumber', 'CompanyName',
        'interestedIn', 'Message', 'read']]


def save_new_leads_for_future(timestamp):
    my_client = get_connection()
    db = use_database(my_client)
    table = get_collection_from_database(db, "leads")
    date_time_for_timestamp = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f")
    time_after_1_second = date_time_for_timestamp + timedelta(seconds=1)
    ts_lower = time.mktime(date_time_for_timestamp.timetuple())
    ts_upper = time.mktime(time_after_1_second.timetuple())
    filter = {
        TableDetails.leads["leads_timestamp"]:
            {"$gte": datetime.fromtimestamp(ts_lower, None), "$lt": datetime.fromtimestamp(ts_upper, None)}
        , TableDetails.leads["leads_module"]: "leads_form"
        , TableDetails.leads["leads_read"]: "0"
    }
    #print(filter)
    result = table.find(filter).sort({TableDetails.leads["leads_timestamp"]: 1}).limit(1)
    #df = pd.json_normalize(result)
    #print(df)
    #TableDetails.leads["leads_timestamp"] = timestamp
    #TableDetails.leads["leads_module"] is leads_form
    #TableDetails.leads["leads_read"] is 0
    if result is None:
        return '[{"userAction": "invalid"}]'
    else:
        new_values = {"$set": {TableDetails.leads["leads_read"]: "2"}}
        update_result = table.update_many(filter, new_values)
        print(update_result.modified_count)
        if update_result.modified_count == 1:
            return '[{"userAction": "successful"}]'
        else:
            return '[{"userAction": "invalid"}]'


def discard_new_leads_now(timestamp):
    my_client = get_connection()
    db = use_database(my_client)
    table = get_collection_from_database(db, "leads")
    date_time_for_timestamp = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f")
    time_after_1_second = date_time_for_timestamp + timedelta(seconds=1)
    ts_lower = time.mktime(date_time_for_timestamp.timetuple())
    ts_upper = time.mktime(time_after_1_second.timetuple())
    filter = {
        TableDetails.leads["leads_timestamp"]:
            {"$gte": datetime.fromtimestamp(ts_lower, None), "$lt": datetime.fromtimestamp(ts_upper, None)}
        , TableDetails.leads["leads_module"]: "leads_form"
        , TableDetails.leads["leads_read"]: "0"
    }
    # print(filter)
    result = table.find(filter).sort({TableDetails.leads["leads_timestamp"]: 1}).limit(1)
    # df = pd.json_normalize(result)
    # print(df)
    # TableDetails.leads["leads_timestamp"] = timestamp
    # TableDetails.leads["leads_module"] is leads_form
    # TableDetails.leads["leads_read"] is 0
    if result is None:
        return '[{"userAction": "invalid"}]'
    else:
        new_values = {"$set": {TableDetails.leads["leads_read"]: "1"}}
        update_result = table.update_many(filter, new_values)
        print(update_result.modified_count)
        if update_result.modified_count == 1:
            return '[{"userAction": "successful"}]'
        else:
            return '[{"userAction": "invalid"}]'


def discard_message_now(timestamp):
    my_client = get_connection()
    db = use_database(my_client)
    table = get_collection_from_database(db, "leads")
    date_time_for_timestamp = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f")
    time_after_1_second = date_time_for_timestamp + timedelta(seconds=1)
    ts_lower = time.mktime(date_time_for_timestamp.timetuple())
    ts_upper = time.mktime(time_after_1_second.timetuple())
    filter = {
        TableDetails.leads["leads_timestamp"]:
            {"$gte": datetime.fromtimestamp(ts_lower, None), "$lt": datetime.fromtimestamp(ts_upper, None)}
        , TableDetails.leads["leads_module"]: "message"
        , TableDetails.leads["leads_read"]: "0"
    }
    # print(filter)
    result = table.find(filter).sort({TableDetails.leads["leads_timestamp"]: 1}).limit(1)
    # df = pd.json_normalize(result)
    # print(df)
    # TableDetails.leads["leads_timestamp"] = timestamp
    # TableDetails.leads["leads_module"] is leads_form
    # TableDetails.leads["leads_read"] is 0
    if result is None:
        return '[{"userAction": "invalid"}]'
    else:
        new_values = {"$set": {TableDetails.leads["leads_read"]: "1"}}
        update_result = table.update_many(filter, new_values)
        print(update_result.modified_count)
        if update_result.modified_count == 1:
            return '[{"userAction": "successful"}]'
        else:
            return '[{"userAction": "invalid"}]'


def discard_saved_leads_now(timestamp):
    my_client = get_connection()
    db = use_database(my_client)
    table = get_collection_from_database(db, "leads")
    date_time_for_timestamp = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f")
    time_after_1_second = date_time_for_timestamp + timedelta(seconds=1)
    ts_lower = time.mktime(date_time_for_timestamp.timetuple())
    ts_upper = time.mktime(time_after_1_second.timetuple())
    filter = {
        TableDetails.leads["leads_timestamp"]:
            {"$gte": datetime.fromtimestamp(ts_lower, None), "$lt": datetime.fromtimestamp(ts_upper, None)}
        , TableDetails.leads["leads_module"]: "leads_form"
        , TableDetails.leads["leads_read"]: "2"
    }
    # print(filter)
    result = table.find(filter).sort({TableDetails.leads["leads_timestamp"]: 1}).limit(1)
    # df = pd.json_normalize(result)
    # print(df)
    # TableDetails.leads["leads_timestamp"] = timestamp
    # TableDetails.leads["leads_module"] is leads_form
    # TableDetails.leads["leads_read"] is 0
    if result is None:
        return '[{"userAction": "invalid"}]'
    else:
        new_values = {"$set": {TableDetails.leads["leads_read"]: "1"}}
        update_result = table.update_many(filter, new_values)
        print(update_result.modified_count)
        if update_result.modified_count == 1:
            return '[{"userAction": "successful"}]'
        else:
            return '[{"userAction": "invalid"}]'


def convert_data_frame_to_json(df):
    json_str = df.to_json(orient="records", date_format='iso')
    return json_str


if __name__ == '__main__':
    pass
    #print(save_leads_from_website())
    #print(fetch_all_leads_and_messages_from_leads_table())
    #save_new_leads_for_future("2025-03-29T10:54:49.501")