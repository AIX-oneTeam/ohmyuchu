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
