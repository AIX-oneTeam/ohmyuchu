from db import Database


def print_day_count():
    collection_histroy = Database.db['day_History']
    total_day_count = collection_histroy.count_documents({})


def save_day_count(token: str):
    collection_histroy = Database.db['day_History']
    collection_user = Database.db['users']

    

    

    
    
