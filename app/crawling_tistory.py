import requests
from bs4 import BeautifulSoup


def get_tistory_content(url):
    # URL 확인
    response = requests.get(url)

    # URL이 적절한지 확인
    if response.status_code != 200:
        return {"error": "URL을 확인해주세요"}
    else:
        soup = BeautifulSoup(response.content, "html.parser")

        # 제목 추출 추가
        title = soup.find(".title-article")
        title_text = title.get_text(strip=True) if title else "제목을 찾을 수 없습니다."

        # 각 콘텐츠 추출 (기존 코드 유지)
        maincontent = soup.select("div.contents_style p")  # 전체 텍스트
        content01 = soup.select("div.contents_style p.og-title")  # 외부 연결 링크 제목
        content02 = soup.select("div.contents_style p.og-desc")  # 외부 연결 링크 내용
        content03 = soup.select("div.contents_style p.og-host")  # 외부 연결 링크 URL

        # 외부 연결 텍스트 리스트(미출력 부분)
        exclude_text = []
        for element in content01:
            exclude_text.append(element.get_text())
        for element in content02:
            text = element.get_text().replace("\xa0", " ").strip()
            exclude_text.append(text)
        for element in content03:
            exclude_text.append(element.get_text())

        # 전체 텍스트 리스트 형식 추출
        final_text = []
        for element in maincontent:
            final_text.append(element.get_text().strip())

        # 필터 후 텍스트 추출
        filtered_list = [item for item in final_text if item not in exclude_text]

        # 필터된 텍스트를 하나의 문자열로 결합
        content = " ".join([text.strip() for text in filtered_list])

        # 크롤링 결과를 올바른 형식으로 반환
        return {
            "title": title_text,
            "content": content,
            "tags": [],  # 티스토리는 태그를 추출하지 않으므로 빈 리스트 반환
        }
