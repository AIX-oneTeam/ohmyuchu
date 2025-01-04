import requests
from bs4 import BeautifulSoup
import re
import emoji


# Velog 게시물의 내용을 크롤링하여 제목, 본문, 태그를 추출하는 함수
def get_velog_content(url):
    """
    주어진 Velog URL에서 게시물의 제목, 본문, 태그를 크롤링하여 반환하는 함수.
    """
    headers = {
        # 웹 크롤링을 위한 User-Agent 설정
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)  # URL로 HTTP GET 요청
    if response.status_code == 200:  # 요청 성공 시
        soup = BeautifulSoup(response.text, "html.parser")  # HTML 파싱

        # 제목 추출
        title = soup.find("h1")  # 제목 태그(h1)를 찾음
        title_text = (
            title.get_text(strip=True) if title else "제목을 찾을 수 없습니다."
        )  # 제목 텍스트 추출

        # 본문 추출
        content = soup.find(
            "div", {"class": "sc-bXTejn FTZwa"}
        )  # 본문이 포함된 div를 찾음
        if content:  # 본문이 존재할 경우
            text = " ".join(content.stripped_strings)  # 본문 텍스트 추출 및 공백 제거
            cleaned_text = re.sub(r"\s+", " ", text).strip()  # 중복 공백 제거
            cleaned_text = emoji.replace_emoji(
                cleaned_text, replace=""
            )  # 텍스트에서 이모지 제거
        else:
            cleaned_text = "본문을 찾을 수 없습니다."  # 본문이 없을 경우

        # 태그 추출
        tags = soup.find_all(
            "a", {"class": "sc-dtMgUX gISUXI"}
        )  # 태그가 포함된 a 태그를 찾음
        tag_list = (
            [tag.get_text(strip=True) for tag in tags] if tags else []
        )  # 태그 텍스트 목록 생성

        # 결과 반환
        return {
            "title": title_text,
            "content": cleaned_text,
            "tags": tag_list,
        }
    else:  # 요청 실패 시
        return {
            "error": f"오류 발생: {response.status_code}"
        }


# 직접 실행 시 테스트 코드
if __name__ == "__main__":
    """
    스크립트를 직접 실행할 때, Velog 게시물 URL을 테스트하여 결과를 출력.
    """
    velog_url = "https://velog.io/@nibble/2024%EB%85%84-%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%A5%BC-%EA%B7%B8%EB%A7%8C%EB%91%94-%EC%82%AC%EB%9E%8C%EC%9D%98-%ED%9A%8C%EA%B3%A0%EA%B8%80"  # 테스트용 Velog URL
    result = get_velog_content(velog_url)
    print(result)