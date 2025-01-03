import requests
from bs4 import BeautifulSoup
import re
import emoji

def get_twitter_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 트윗 내용 추출
        tweet_content = soup.find('div', {'data-testid': 'tweetText'})
        tweet_text = tweet_content.get_text(strip=True) if tweet_content else '트윗 내용을 찾을 수 없습니다.'
        
        # 사용자 이름 추출
        user_info = soup.find('div', {'class': 'css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3'})
        user_name = user_info.get_text(strip=True) if user_info else '사용자 정보를 찾을 수 없습니다.'
        
        # 텍스트 클리닝 (이모지 및 공백 제거)
        cleaned_text = re.sub(r'\s+', ' ', tweet_text).strip()
        cleaned_text = emoji.replace_emoji(cleaned_text, replace='')
        
        return {
            'user_name': user_name,
            'content': cleaned_text
        }
    else:
        return {'error': f'오류 발생: {response.status_code}'}

# 직접 실행시 테스트용
if __name__ == "__main__":
    twitter_url = 'https://x.com/gomdol350799'
    result = get_twitter_content(twitter_url)
    print(result)
