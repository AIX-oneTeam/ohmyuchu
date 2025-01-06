# from motor.motor_asyncio import AsyncIOMotorClient
import random

async def get_comment(emotion: str, comment_collection) -> str:
    """
    입력된 감정에 해당하는 코멘트를 MongoDB에서 가져와 랜덤으로 반환하는 함수입니다.

    Args:
        emotion (str): 감정 이름 (예: '기쁨', '슬픔', '놀람', '분노', '공포', '혐오', '중립')

    Returns:
        str: 해당 감정에 맞는 코멘트 문자열
    """
    # MongoDB에서 해당 감정의 코멘트 리스트를 가져옵니다.
    comment_data = await comment_collection.find_one({"emotion": emotion})
    print(comment_data)

    if not comment_data:
        return "해당 감정에 대한 코멘트를 찾을 수 없습니다."

    return random.choice(comment_data["comment"])
    
    # if comment_data and "comment" in comment_data:
    #     # 코멘트 리스트에서 랜덤으로 하나 선택하여 반환
    #     return random.choice(comment_data["comment"])
    # else:
    #     return "해당 감정에 대한 코멘트를 찾을 수 없습니다."

# if __name__ == "__main__":
#     import asyncio

#     async def main():
#         client = AsyncIOMotorClient("mongodb://localhost:27017")
#         db = client["test_db"]
#         comment_collection = db["comments"]

#         test_emotion = "기쁨"
#         result = await get_comment(test_emotion, comment_collection)
#         print(f"결과: {result}")

#     asyncio.run(main())
