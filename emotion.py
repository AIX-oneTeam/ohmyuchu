from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# 모델과 토크나이저 로드
model_name = "hun3359/klue-bert-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# 새로운 감정 그룹화
id2label = {
    "0": "분노", "1": "좌절한", "2": "방어적인", "3": "안달하는",
    "4": "성가신", "5": "슬픔", "6": "비통한", "7": "우울한",
    "8": "낙담한", "9": "불안", "10": "스트레스 받는",
    "11": "혼란스러운", "12": "회의적인", "13": "조심스러운",
    "14": "상처", "15": "배신당한", "16": "충격 받은",
    "17": "억울한", "18": "괴로워하는", "19": "당황",
    "20": "외로운", "21": "죄책감의", "22": "부끄러운",
    "23": "한심한", "24": "기쁨", "25": "편안한",
    "26": "만족스러운", "27": "안도", "28": "자신하는", "29": "희망"
}

# 새로운 label2id 생성
label2id = {v: k for k, v in id2label.items()}

# 모델 설정에 추가
model.config.id2label = id2label
model.config.label2id = label2id

# 분석할 문장
text = "오십에 시작하는 마음 공부 저자 김종원 출판 비즈니스북스 발매 2023.02.24. ​ 세상에는 급하게 원하는 것을 취하려는 사람이 많다. 연암에게도 그런 사람들이 자주 찾아와 방법을 구했다. 그럴 때마다 연암은 그들의 성급한 마음을 진정시키면서 “지금 어떻게 공부를 하고 있는가?”라고 물었다. 그들은 모두 달랐지만, 내놓은 답은 하나로 귀결됐다. ​ “다른 이들보다 더 많이 읽고, 빠르게 이해가 되지 않으면 어떻게든 외워서라도 알려고 노력합니다.” ​ 언뜻 들으면 공부를 매우  잘하고 있는 것처럼 보인. 그러나 생각이 전혀 달랐던 연암은 “앞으로 공부법을 바꾸는 게 좋겠다.”라고 조언하며 그 이유에 대해 이렇게 말했다. “많이 읽고 무작정 외우는 것은 최선의 방법이 아니다. 비록 하나를 알더라도 그 하나를 제대로 음미하고 면밀하게 생각하는 것이 중요하다.” 연암이 인생 후반기에 흔들리지 않고 처음의 마음을 지킬 수 있었던 힘도 바로 “뭐든 제대로 익혀서 내 것으로 만들며 살아가는 일상이 중요하다.”라는 철학에 있다. ​ <오십에 시작하는 마음공부> 중에서 책 읽으며 세상 공부를 시작한 게 마흔셋이었습니다. 늦은 시작이라고 할 수 있습니다. 장점보다 단점이 더 많은 것 같습니다. 무엇보다 조급함입니다. 늦은 만큼 빨리 가고 싶은 마음이죠. 누가 뒤에서 쫓아오는 것도 아닌데 말이 죠. 혼자만의 착각에 빠져 성급하게 무언가 해야 할 것 같습니다. 사실은 뒤에 아무도 없고 누구도 빨리하라고 말하지 않는데 말이죠. 아마도 새롭게 시작한다는 각오가 태도를 만드는 것 같습니다. ​ 저도 이제까지 성급하게 책을 읽어 왔습니다. 일 년 동안 300권 읽기에 도전했었습니다."

# 토큰화
inputs = tokenizer(text, return_tensors="pt")

# 모델 추론
with torch.no_grad():
    outputs = model(**inputs)

# 결과 해석
logits = outputs.logits
predicted_class_id = torch.argmax(logits, dim=-1).item()
predicted_label = model.config.id2label[str(predicted_class_id)]

print(f"문장: {text}")
print(f"예측된 감정: {predicted_label}")
