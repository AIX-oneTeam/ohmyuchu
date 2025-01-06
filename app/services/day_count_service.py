from datetime import datetime, timezone
from db import Database


async def print_day_count():
    collection_histroy = Database.db['history']

    # 하루 기준 집계
    today = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    today_count = await collection_histroy.count_documents({"timestamp": {"$gte": today}})
    total_count = await collection_histroy.count_documents({})
    anonymous_count = await collection_histroy.count_documents({"email": "anonymous"})

    if(total_count and anonymous_count):
        user_count = total_count - anonymous_count
        return {
        "total_count": total_count,
        "user_count": user_count,
        "anonymous_count": anonymous_count,
        "today_count": today_count
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



    

    

    
    
