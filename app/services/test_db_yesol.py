from pymongo import MongoClient

# MongoDB 연결 설정
mongoDB_url: str = "mongodb://192.168.0.141:27017"
database_name: str = "ohmyuchu"

client = MongoClient(mongoDB_url)  # 적절한 MongoDB URI로 교체
db = client[database_name]  # 데이터베이스 이름
songs = db['songs']  # 컬렉션 이름

# 저장할 데이터
# song_data = {
#     "title": "UGH!",
#     "artist": "BTS",
#     "url": "https://youtu.be/y-0QlQH5d3Y?si=OSKyMEDakboozK-F",
#     "emotion_keyword": "분노",
#     "play_count": 0,
#     "like_count": 0,
#     "dislike_count": 0
# }
song_data = {
    "title": "삐딱하게",
    "artist": "G-DRAGON",
    "url": "https://youtu.be/RKhsHGfrFmY?si=9cx7n_BHBfSDQXo7",
    "emotion_keyword": "분노",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
}
# 데이터 삽입
result = songs.insert_one(song_data)

# 삽입 결과 확인
print(f"Inserted document ID: {result.inserted_id}")


##############
from pymongo import MongoClient
from bson import ObjectId  # ObjectId를 임포트

# MongoDB 연결 설정
comments = db['comments']  # 컬렉션 이름

# 저장할 데이터
message_data = {
  "emotion_keyword": "분노",
  "comments": [
    "힘든 하루를 보내셨네요. 노래를 들으며 기분을 해소해봐요!",
    "강렬한 비트와 에너지로 스트레스를 해소해봐요!"
  ]
}
# 데이터 삽입
result = comments.insert_one(message_data)

# 삽입 결과 확인
print(f"Inserted document ID: {result.inserted_id}")

##########

from pymongo import MongoClient
from datetime import datetime

logs = db['logs']  # logs 컬렉션

# 저장할 데이터
log_data = {
    "domain": "naver",
    "emotion": "분노",
    "song_title": "UGH!",
    "feedback": "like",
    "use_time": datetime.now()  # 현재 시간
}

# 데이터 삽입
result = logs.insert_one(log_data)

# 삽입 결과 확인
print(f"Inserted log document ID: {result.inserted_id}")

######

from pymongo import MongoClient
from datetime import datetime

analystics = db['analystics']  # logs 컬렉션

# 저장할 데이터
analystics_data = {
  "emotions" : {
      "분노": 1
  }
}

# 데이터 삽입
result = analystics.insert_one(analystics_data)

# 삽입 결과 확인
print(f"Inserted log document ID: {result.inserted_id}")

