import pandas as pd


DATA_POPULAR_PRODUCTS_URL = "https://drive.google.com/file/d/14pjKO4bm0HFI3NiZULy_3qK23tUSAvL8/view?usp=sharing"
DATA_PRODUCT_CART_URL = "https://drive.google.com/file/d/1o2ShUmVY-VmTuE3gZVvD0VoMYx8eDVKw/view?usp=sharing"
DATA_INVENTORY_URL ="https://drive.google.com/file/d/1WR-CI07hntH9gvY6ukCESUXqrQzkoHd3/view?usp=sharing"
DATA_PRODUCT_WISHLIST_URL = "https://drive.google.com/file/d/16ZycJ9wJBcmFjwbDUT_zUxIkRee79Amb/view?usp=sharing"


def fetch_data_based_on_query(query):
    json_str = ""
    if query == "popularProduct":
        df = read_file_from_drive(DATA_POPULAR_PRODUCTS_URL)
        json_str = convert_data_frame_to_json(df)
    elif query == "myCart":
        df = read_file_from_drive(DATA_PRODUCT_CART_URL)
        json_str = convert_data_frame_to_json(df)
    elif query == "myWishlist":
        df = read_file_from_drive(DATA_PRODUCT_WISHLIST_URL)
        json_str = convert_data_frame_to_json(df)
    elif query == "productInventory":
        df = read_file_from_drive(DATA_INVENTORY_URL)
        json_str = convert_data_frame_to_json(df)
    else:
        json_str = '{"message":"Hello World!"}'
    return json_str


def read_file_from_drive(url):
    url = 'https://drive.google.com/uc?id=' + url.split('/')[-2]
    df = pd.read_csv(url, header=None)
    '''Set first row as header'''
    df.columns = df.iloc[0]
    df = df[1:]
    return df


def convert_data_frame_to_xml(df):
    xml_str = df.to_xml()
    return xml_str


def convert_data_frame_to_json(df):
    json_str = df.to_json(orient="records")
    return json_str

if __name__ == '__main__':
    fetch_data_based_on_query("popularProduct")
