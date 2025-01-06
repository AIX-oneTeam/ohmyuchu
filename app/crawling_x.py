from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_x_content(url: str) -> dict:
    """
    주어진 트윗 URL에서 제목, 내용, 태그를 추출하여 반환하는 함수.

    Args:
        url (str): 트윗 URL

    Returns:
        dict: 트윗의 제목, 내용, 태그
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # 브라우저 창을 띄우지 않음
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # ChromeDriver 서비스 객체 생성
    service = Service(ChromeDriverManager().install())

    # Chrome WebDriver 생성
    driver = webdriver.Chrome(service=service, options=options)

    title = "X 게시글"  # 트윗의 제목 (기본값)
    content = ""        # 트윗 내용
    tags = []           # 태그 목록 (현재는 비어 있음)

    try:
        # 트윗 URL로 이동
        driver.get(url)
        time.sleep(5)  # 페이지 로드 및 JS 렌더링 대기

        # data-testid="tweetText" 요소를 찾아 텍스트 추출
        tweet_div = driver.find_element("xpath", "//div[@data-testid='tweetText']")
        content = tweet_div.text

    except Exception as e:
        print(f"[오류 발생] {e}")
        title = "오류 발생"  # 오류 발생 시 제목 변경
        content = f"오류 발생: {e}"  # 오류 메시지를 content로 반환
    finally:
        driver.quit()  # 브라우저 닫기

    return {
        "title": title,
        "content": content,
        "tags": tags  # 현재는 태그를 추출하지 않으므로 빈 리스트를 반환
    }


# 직접 실행 시 테스트 코드
if __name__ == "__main__":
    test_url = "https://x.com/gomdol350799/status/1874704689452970254"
    result = get_x_content(test_url)
    print(result)
