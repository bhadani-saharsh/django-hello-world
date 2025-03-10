import pymongo
from bson.objectid import ObjectId
import pandas as pd

import TableDetails


def get_connection():
    uri = TableDetails.DATA_BASE_URI
    my_client = pymongo.MongoClient(uri)
    # print(my_client)
    return my_client


def use_database(my_client):
    db = my_client[TableDetails.DATE_BASE_NAME]
    return db


def get_collection_from_database(db, table_name):
    return db[table_name]


def get_results_for_user_name(table, user_name, password):
    result = table.find_one({TableDetails.USER_TABLE["USER_EMAIL"] : user_name, TableDetails.USER_TABLE["USER_PASSWORD"] : password})
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


def convert_data_frame_to_json(df):
    json_str = df.to_json(orient="records")
    return json_str


if __name__ == '__main__':
    pass