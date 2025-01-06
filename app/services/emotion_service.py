from transformers import AutoTokenizer, AutoConfig, BertForSequenceClassification
import torch
from fastapi import FastAPI, Form, Request
from fastapi.responses import JSONResponse


# 모델 및 토크나이저 초기화
model_name = "monologg/kobert"
tokenizer = AutoTokenizer.from_pretrained("monologg/kobert", trust_remote_code=True)  # KoBertTokenizer 사용
config = AutoConfig.from_pretrained(model_name)
config.num_labels = 7
config.id2label = {
    0: "기쁨",
    1: "슬픔",
    2: "놀람",
    3: "분노",
    4: "공포",
    5: "혐오",
    6: "중립"
}
config.label2id = {v: k for k, v in config.id2label.items()}
model = BertForSequenceClassification.from_pretrained(
    model_name, config=config, ignore_mismatched_sizes=True 
)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# 감정 분석 함수
def analyze_emotion(text: str) -> str:
    """
    입력 텍스트에 대해 감정 분석을 수행하고 결과를 반환합니다.
    """
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,  # 긴 텍스트 자르기
        max_length=512,   # 최대 512 토큰
        padding="max_length"  # 고정된 길이로 패딩
    ).to(device)

    model.eval()
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=-1).item()
    
    print(f"Predicted class: {predicted_class}")
    # 감정 결과 반환
    return config.id2label[predicted_class]

