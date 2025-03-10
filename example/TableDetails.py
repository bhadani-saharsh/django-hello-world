DATE_BASE_NAME = "ecomm"

DATA_BASE_URI = "mongodb+srv://saharshbhadani:EHzqD6WK0OTbk9jB@cluster0.pella.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

USER_TABLE = {
    "USER_USER_ID": "userID",
    "USER_FULL_NAME": "fullName",
    "USER_USER_TYPE": "userType",
    "USER_EMAIL": "email",
    "USER_PHONE_NUMBER": "phoneNumber",
    "USER_PASSWORD": "password",
    "USER_REGISTERED_ON": "registeredOn",
    "USER_DATE_OF_BIRTH": "dateOfBirth",
    "USER_LAST_LOGIN": "lastLogin",
    "USER_PROFILE_PHOTO": "profilePhoto"
}

STORE_DETAILS = {
    "STORE_DETAILS_STORE_ID": "storeID",
    "STORE_DETAILS_USER_ID": "userID",
    "STORE_DETAILS_STORE_NAME": "storeName",
    "STORE_DETAILS_REGISTERED_ON": "registeredOn",
    "STORE_DETAILS_DATE_OF_INCORPORATION": "dateOfIncorporation",
    "STORE_DETAILS_LAST_LOGIN": "lastLogin",
    "STORE_DETAILS_STORE_PHOTO": "storePhoto"
}

CATEGORY = {
    "CATEGORY_PRODUCT_CATEGORY_ID": "ProductCategoryID",
    "CATEGORY_PRODUCT_CATEGORY": "ProductCategory",
    "CATEGORY_THUMBNAIL_ID": "ThumbnailID",
    "CATEGORY_PRODUCT_CATEGORY_DESCRIPTION": "ProductCategoryDescription"
}

PRODUCT = {
    "PRODUCT_PRODUCT_ID": "ProductID",
    "PRODUCT_PRODUCT_NAME": "ProductName",
    "PRODUCT_PRODUCT_CATEGORY": "ProductCategory",
    "PRODUCT_SUB_CATEGORY": "SubCategory",
    "PRODUCT_MANUFACTURED_BY": "ManufacturedBy",
    "PRODUCT_PRODUCT_DESCRIPTION": "ProductDescription"
}

PRODUCT_VARIANT = {
    "PRODUCT_VARIANT_PRODUCT_VARIANT_ID": "Product_variant_ID",
    "PRODUCT_VARIANT_PRODUCT_ID": "ProductID",
    "PRODUCT_VARIANT_QUANTITY_HELD": "QuantityHeld",
    "PRODUCT_VARIANT_QUANTITY_SOLD": "QuantitySold",
    "PRODUCT_VARIANT_BEST_BEFORE": "BestBefore",
    "PRODUCT_VARIANT_VENDOR": "Vendor",
    "PRODUCT_VARIANT_LOCATION": "Location",
    "PRODUCT_VARIANT_INVENTORY_ADDITION_DATE": "InventoryAdditionDate",
    "PRODUCT_VARIANT_LISTED_BY": "ListedBy",
    "PRODUCT_VARIANT_VARIATION_TYPE": "variation_type",
    "PRODUCT_VARIANT_VARIATION_VALUE": "variation_value",
    "PRODUCT_VARIANT_PRICE": "Price",
    "PRODUCT_VARIANT_THUMBNAIL_ID": "ThumbnailID",
    "PRODUCT_VARIANT_PICTURE_ID": "PictureID"
}

STORE_OFFERS_PRODUCT_VARIANT = {
    "STORE_OFFERS_PRODUCT_VARIANT_STORE_ID": "storeID",
    "STORE_OFFERS_PRODUCT_VARIANT_PRODUCT_VARIANT_ID": "Product_variant_ID",
    "STORE_OFFERS_PRODUCT_VARIANT_PRICE": "Price",
    "STORE_OFFERS_PRODUCT_VARIANT_DISCOUNT_TYPE": "DiscountType",  # amount or percentage or none
    "STORE_OFFERS_PRODUCT_VARIANT_DISCOUNT_VALUE": "DiscountValue",
    "STORE_OFFERS_PRODUCT_VARIANT_DISCOUNTED_PRICE": "DiscountedPrice",
    "STORE_OFFERS_PRODUCT_VARIANT_VALIDITY": "validity",
    "STORE_OFFERS_PRODUCT_VARIANT_PICTURE_ID": "PictureID"
}

CART = {
    "CART_CART_ID": "CartID",
    "CART_USER_ID": "userID",
    "CART_PRODUCT_VARIANT_ID": "Product_variant_ID",
    "CART_QUANTITY": "Quantity",
    "CART_STORE_ID": "storeID",
    "CART_MODIFIED_DATE": "modifiedDate"
}

POPULAR_CATEGORIES = {
    "POPULAR_CATEGORIES_POPULAR_CATEGORIES_ID": "Popular_categories_ID",
    "POPULAR_CATEGORIES_USER_ID": "userID",
    "POPULAR_CATEGORIES_PRODUCT_CATEGORY": "ProductCategory",
    "POPULAR_CATEGORIES_THUMBNAIL_ID": "ThumbnailID"
}
