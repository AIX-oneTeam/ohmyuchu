import requests
from bs4 import BeautifulSoup
import re
import emoji

def get_velog_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 제목 추출
        title = soup.find('h1')
        title_text = title.get_text(strip=True) if title else '제목을 찾을 수 없습니다.'
        
        # 본문 추출
        content = soup.find('div', {'class': 'sc-bXTejn FTZwa'})
        if content:
            text = ' '.join(content.stripped_strings)
            cleaned_text = re.sub(r'\s+', ' ', text).strip()
            cleaned_text = emoji.replace_emoji(cleaned_text, replace='')
        else:
            cleaned_text = '본문을 찾을 수 없습니다.'
        
        # 태그 추출
        tags = soup.find_all('a', {'class': 'sc-dtMgUX eUxucx'})
        tag_list = [tag.get_text(strip=True) for tag in tags] if tags else []
        
        return {
            'title': title_text,
            'content': cleaned_text,
            'tags': tag_list
        }
    else:
        return {'error': f'오류 발생: {response.status_code}'}

# 직접 실행시 테스트용
if __name__ == "__main__":
    velog_url = 'https://velog.io/@nibble/2024%EB%85%84-%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%A5%BC-%EA%B7%B8%EB%A7%8C%EB%91%94-%EC%82%AC%EB%9E%8C%EC%9D%98-%ED%9A%8C%EA%B3%A0%EA%B8%80'
    result = get_velog_content(velog_url)
    print(result)