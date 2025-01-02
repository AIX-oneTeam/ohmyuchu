# from fastapi import APIRouter, Request
# from app.services.user_service import get_user_data
# from fastapi.templating import Jinja2Templates

# router = APIRouter()

# # 템플릿 파일 폴더 경로 설정
# templates = Jinja2Templates(directory="app/templates")

# @router.get("/user/{user_id}")
# async def user_profile(request: Request, user_id: int):
#     user = get_user_data(user_id)
#     return templates.TemplateResponse("user_template.html", {"request": request, "user": user})
