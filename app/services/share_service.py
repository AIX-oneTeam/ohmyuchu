from fastapi import HTTPException
import pyperclip
from playwright.async_api import async_playwright
from PIL import Image
import base64
import io

async def capture_page():
    """
    특정 URL의 특정 요소를 캡처하고 Base64로 반환
    """
    try:
        async with async_playwright() as p:
            url = "http://127.0.0.1:8000/v1/models/summary" # 결과 페이지 URL
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(url)

            class_name = "ret_text_container"
            # 요소 스크린샷
            element = await page.query_selector(f".{class_name}")
            if not element:
                raise HTTPException(status_code=404, detail="Element not found")

            # 요소의 스크린샷 캡처
            screenshot = await element.screenshot(type="png")

            # Base64 인코딩
            buffered = io.BytesIO(screenshot)
            base64_image = base64.b64encode(buffered.getvalue()).decode("utf-8")

            # 클립보드에 복사
            pyperclip.copy(base64_image)

            await browser.close()

            return {"image_base64": base64_image}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
