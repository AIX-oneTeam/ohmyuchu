import praw
from transformers import BertTokenizer, BertForSequenceClassification, AutoConfig
import torch

# 감정 분석 함수
def analyze_sentiment(text):
    # KLUE-BERT 모델 로드
    model_name = "hun3359/klue-bert-base-sentiment"
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertForSequenceClassification.from_pretrained(model_name)
    config = AutoConfig.from_pretrained(model_name)  # id2label 딕셔너리 가져오기

    # 입력 텍스트 토큰화
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    
    # 모델에 입력 텍스트 전달
    outputs = model(**inputs)
    logits = outputs.logits
    probabilities = torch.softmax(logits, dim=1)
    
    # 예측값 처리
    sentiment_id = torch.argmax(probabilities).item()  # 예측된 클래스 ID
    print(f"Predicted sentiment ID: {sentiment_id}")  # 디버깅용 출력
    
    # 감정 라벨 매핑 (정수형 키 사용)
    sentiment_label = config.id2label.get(sentiment_id, "unknown")  # 정수형 그대로 사용
    sentiment_score = probabilities[0][sentiment_id].item()  # 신뢰도 점수
    
    return sentiment_label, sentiment_score

# Reddit 게시물 가져오기 및 감정 분석
def get_user_posts_and_analyze():
    try:
        # Reddit 인스턴스 생성
        reddit = praw.Reddit(
            client_id="",
            client_secret="",
            user_agent="",
        )

        # 특정 사용자의 게시물 가져오기
        username = "gomting_02"
        print(f"Fetching posts from user: {username}")
        user = reddit.redditor(username)
        
        # 최신 게시물 1개 가져오기
        for submission in user.submissions.new(limit=1):
            print("\nPost found:")
            print(f"Title: {submission.title}")
            print(f"Content: {submission.selftext}")  # 게시글 내용
            print(f"Score: {submission.score}")
            print(f"URL: {submission.url}")
            print("-" * 50)
            
            # 감정 분석 수행
            text = submission.selftext 
            sentiment, score = analyze_sentiment(text)
            
            # 감정 분석 결과 출력
            print(f"Predicted Emotion: {sentiment}")
            print("-" * 50)

    except Exception as e:
        print(f"Error occurred: {type(e).__name__}: {str(e)}")
        print(f"Full error details: {str(e)}")

if __name__ == "__main__":
    get_user_posts_and_analyze()
