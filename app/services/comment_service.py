import random
from pymongo import MongoClient

# MongoDB 연결 설정
mongoDB_url: str = "mongodb+srv://ohmyuchu:ohmyuchu1111@test.9r2s8.mongodb.net/"
database_name: str = "test"

client = MongoClient(mongoDB_url)
db = client[database_name]
comment_collection = db['comment']  # 'comment' 컬렉션

def get_comment(emotion: str) -> str:
    """
    입력된 감정에 해당하는 코멘트를 MongoDB에서 가져와 랜덤으로 반환하는 함수입니다.

    Args:
        emotion (str): 감정 이름 (예: '기쁨', '슬픔', '놀람', '분노', '공포', '혐오', '중립')

    Returns:
        str: 해당 감정에 맞는 코멘트 문자열
    """
    # MongoDB에서 해당 감정의 코멘트 리스트를 가져옵니다.
    comment_data = comment_collection.find_one({"emotion": emotion})

    if comment_data and "comment" in comment_data:
        # 코멘트 리스트에서 랜덤으로 하나 선택하여 반환
        return random.choice(comment_data["comment"])
    else:
        return "해당 감정에 대한 코멘트를 찾을 수 없습니다."

# 테스트 코드 (선택사항)
if __name__ == "__main__":
    test_emotion = "분노"  # 테스트할 감정 입력
    comment = get_comment(test_emotion)
    print(f"감정: {test_emotion}, 코멘트: {comment}")
