import requests
from bs4 import BeautifulSoup
import re
import emoji

def get_blog_content(url):
    """
    네이버 블로그 URL에서 제목과 본문을 크롤링하여 반환합니다.
    """
    # 모바일 URL로 변환
    mobile_url = url.replace('blog.naver.com', 'm.blog.naver.com')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(mobile_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # 제목 추출
        title = soup.find('div', {'class': 'se_textarea'})
        title_text = title.get_text(strip=True) if title else '제목을 찾을 수 없습니다.'

        # 본문 추출
        content = soup.find('div', {'class': 'se-main-container'})
        if content:
            # 텍스트 추출 및 공백 정리
            text = ' '.join(content.stripped_strings)
            cleaned_text = re.sub(r'\s+', ' ', text).strip()

            # 불필요한 문자열 제거
            unwanted_strings = ['blog.naver.com', 'search.naver.com', 'open.kakao.com']
            for unwanted in unwanted_strings:
                cleaned_text = cleaned_text.replace(unwanted, '').strip()

            # 이모티콘 제거
            cleaned_text = emoji.replace_emoji(cleaned_text, replace='')
        else:
            cleaned_text = '본문을 찾을 수 없습니다.'

        # 결과 반환
        return {
            'title': title_text,
            'content': cleaned_text
        }
    else:
        return {'error': f'오류 발생: {response.status_code}'}


# 직접 실행 시 테스트용 코드
if __name__ == "__main__":
    test_url = 'https://blog.naver.com/loveyou12/223714493311'  # 테스트할 네이버 블로그 URL
    result = get_blog_content(test_url)

    if 'error' in result:
        print("오류:", result['error'])
    else:
        print("제목:", result['title'])
        print("\n본문:")
        print(result['content'])