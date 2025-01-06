from datetime import datetime, timezone
from db import Database


def print_day_count():
    collection_histroy = Database.db['history']
    total_count = collection_histroy.count_documents({})
    aonymous_count = collection_histroy.count_documents({"email": "anonymous"})
    user_count = total_count - aonymous_count

    return {
        "total_count": total_count,
        "user_count": user_count,
        "anonymous_count": aonymous_count
    }


def save_day_count(userInfo: dict):
    collection_histroy = Database.db['history']
    # current_time = datetime.now()
    # formatted_time = current_time.strftime("%Y-%m-%d")
    current_time = datetime.now(timezone.utc)

    email = userInfo.get('email', 'anonymous')
    nickname = userInfo.get('nickname', 'anonymous')

    user_history = {
        "email": email,
        "nickname": nickname,
        "timestamp": current_time
    }

    print(user_history)
    collection_histroy.insert_one(user_history)



    

    

    
    
