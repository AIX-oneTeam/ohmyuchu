import requests
from bs4 import BeautifulSoup
import re
import emoji

def get_blog_content(url):
    # 모바일 URL로 변환
    mobile_url = url.replace('blog.naver.com', 'm.blog.naver.com')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(mobile_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 이미지 태그 제거
        for img in soup.find_all('img'):
            img.decompose()
        
        # 본문 추출
        content = soup.find('div', {'class': 'se-main-container'})
        if content:
            # 텍스트 추출 및 공백 정리
            text = ' '.join(content.stripped_strings)
            # 연속된 공백 및 개행 문자 제거
            cleaned_text = re.sub(r'\s+', ' ', text).strip()
            # 불필요한 문자열 제거
            unwanted_strings = ['blog.naver.com', 'search.naver.com','open.kakao.com']
            for unwanted in unwanted_strings:
                cleaned_text = cleaned_text.replace(unwanted, '').strip()
            # 이모티콘 제거
            cleaned_text = emoji.replace_emoji(cleaned_text, replace='')
            return cleaned_text
        else:
            return '본문을 찾을 수 없습니다.'
    else:
        return f'오류 발생: {response.status_code}'

# 사용 예시
blog_url = 'https://blog.naver.com/motifree33/223712187313'
print(get_blog_content(blog_url))
