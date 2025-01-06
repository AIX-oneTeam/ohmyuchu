from fastapi import APIRouter, Query, Request
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
import httpx
from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수에서 키 가져오기
KAKAO_CLIENT_ID = os.getenv("KAKAO_CLIENT_ID")
KAKAO_REDIRECT_URI = os.getenv("KAKAO_REDIRECT_URI")
mongoDB_url = os.getenv("mongoDB")

# MongoDB 설정
database_name = "test"
client = MongoClient(mongoDB_url)
db = client[database_name]
user_collection = db["user"]

router = APIRouter()
templates = Jinja2Templates(directory="templates")  # templates 폴더 위치 지정

# Kakao REST API 설정
KAKAO_TOKEN_URL = "https://kauth.kakao.com/oauth/token"
KAKAO_USERINFO_URL = "https://kapi.kakao.com/v2/user/me"

@router.get("/login")
def kakao_login():
    """
    카카오 로그인 URL로 리다이렉트합니다.
    """
    kakao_oauth_url = (
        f"https://kauth.kakao.com/oauth/authorize"
        f"?client_id={KAKAO_CLIENT_ID}&redirect_uri={KAKAO_REDIRECT_URI}&response_type=code"
    )
    return RedirectResponse(kakao_oauth_url)

@router.get("/callback")
async def kakao_callback(request: Request, code: str = Query(...)):
    """
    카카오 로그인 인증 후 사용자 정보를 가져오고 MongoDB에 저장.
    """
    try:
        # 1. Access Token 요청
        async with httpx.AsyncClient() as client:
            token_response = await client.post(
                KAKAO_TOKEN_URL,
                data={
                    "grant_type": "authorization_code",
                    "client_id": KAKAO_CLIENT_ID,
                    "redirect_uri": KAKAO_REDIRECT_URI,
                    "code": code,
                },
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )

        token_json = token_response.json()
        if token_response.status_code != 200 or "error" in token_json:
            return JSONResponse(content={"message": "INVALID_CODE"}, status_code=400)

        access_token = token_json.get("access_token")

        # 2. 사용자 정보 요청
        async with httpx.AsyncClient() as client:
            profile_response = await client.get(
                KAKAO_USERINFO_URL,
                headers={"Authorization": f"Bearer {access_token}"},
            )

        profile_data = profile_response.json()
        if profile_response.status_code != 200 or "id" not in profile_data:
            return JSONResponse(content={"message": "INVALID_TOKEN"}, status_code=400)

        # 3. 사용자 정보 반환
        user_info = {
            "id": str(profile_data.get("id")),
            "nickname": profile_data["kakao_account"]["profile"]["nickname"],
            "email": profile_data["kakao_account"].get("email"),
        }

        # 확인용
        print("사용자 정보:", user_info)

        # 4. MongoDB에 사용자 정보 저장
        try:
            existing_user = user_collection.find_one({"email": user_info["email"]})
            if not existing_user:
                result = user_collection.insert_one(user_info)
                print(f"저장 성공: {result.inserted_id}")
            else:
                print(f"기존 회원: {user_info['email']} 로그인 처리 완료.")
        except Exception as e:
            print(f"데이터 처리 중 오류 발생: {str(e)}")
            return JSONResponse(content={"message": f"DB_ERROR: {str(e)}"}, status_code=500)

        # 5. 토큰과 함께 템플릿 렌더링
        return templates.TemplateResponse(
            "auth_loading.html",  # 로딩용 페이지
            {
                "request": request,
                "kakao_token": access_token
            }
        )

    except Exception as e:
        return JSONResponse(content={"message": str(e)}, status_code=400)