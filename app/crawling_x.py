from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_tweet_text(tweet_url: str) -> str:
    options = webdriver.ChromeOptions()
    options.add_argument("--headless") 
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # service 객체를 따로 생성
    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)

    tweet_text = ""
    try:
        driver.get(tweet_url)
        time.sleep(5)  # 페이지 로드 & JS 렌더링 대기

        # data-testid="tweetText" 요소 찾아서 텍스트 추출
        tweet_div = driver.find_element("xpath", "//div[@data-testid='tweetText']")
        tweet_text = tweet_div.text

    except Exception as e:
        print(f"[오류 발생] {e}")
    finally:
        driver.quit()

    return tweet_text

if __name__ == "__main__":
    url = input("트윗 URL을 입력하세요: ")
    print(get_tweet_text(url))
