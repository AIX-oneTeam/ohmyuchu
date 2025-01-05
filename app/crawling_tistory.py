import requests
from bs4 import BeautifulSoup


#티스토리 텍스트 추출 함수
def get_tistory_content(url):

    # URL 입력
    # url = 'https://michan1027.tistory.com/2595'

    # URL 확인
    response = requests.get(url)

    # URL이 적절한지 확인 
    if response.status_code != 200:
        print("url을 확인해주세요")
    else:
        soup = BeautifulSoup(response.content, 'html.parser')

        # 각 콘텐츠 추출
        maincontent = soup.select('div.contents_style p')  # 전체 텍스트
        content01 = soup.select('div.contents_style p.og-title')  # 외부 연결 링크 제목
        content02 = soup.select('div.contents_style p.og-desc')  # 외부 연결 링크 내용
        content03 = soup.select('div.contents_style p.og-host')  # 외부 연결 링크 URL

        # 외부 연결 텍스트 리스트(미출력 부분)
        exclude_text = []
        for element in content01:
            exclude_text.append(element.get_text())
        for element in content02:
            text = element.get_text().replace('\xa0', ' ').strip()
            exclude_text.append(text)
        for element in content03:
            exclude_text.append(element.get_text())

        # 외부 연결 제목 확인용 출력 
        print("---중간 연결 제목---")          
        for element in content01:
            print(element.get_text().strip())

        # 외부 연결 내용 확인용 출력
        print("---중간 연결 내용 ---")
        for element in content02:
            print(element.get_text().strip())

        # 미출력 합 리스트 형식 확인용 출력
        print('---미출력 합 리스트 형식 출력---')   
        print(exclude_text)

        # 전체 텍스트 리스트 형식 추출
        print("---전체텍스트 리스트 형식 추출---")
        final_text = []
        for element in maincontent:
            final_text.append(element.get_text().strip())
        print(final_text)

        # 전체 부분 출력 (필터 전)
        print("---전체텍스트(필터 전) 리스트 형식 출력---")
        final_text = []
        for element in maincontent:
            final_text.append(element.get_text().strip())
        print(final_text)

        # 필터 후 텍스트 출력
        print("---전체텍스트(필터 후) 리스트 형식 출력---")
        filtered_list = [item for item in final_text if item not in exclude_text]

        for text in filtered_list:
            print(text.strip())

        return {
            text.strip()
        }    