from typing import Callable, Dict
import torch
from transformers import PreTrainedTokenizerFast, BartForConditionalGeneration
from crawling_velog import get_velog_content


# 텍스트 전처리 함수: 텍스트를 요약 전 필요한 전처리를 수행
def preprocess_text(text):
    """
    텍스트 전처리 함수
    - 텍스트의 첫 번째 문단을 추출하고 본문에 포함
    - 텍스트를 줄 단위로 나누고, 공백을 제거하여 다시 병합
    """
    first_paragraph = text.split("\n")[0]  # 첫 번째 문단 추출
    text = first_paragraph + ". " + text  # 첫 문단을 본문 앞에 추가
    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]  # 빈 문단 제거
    text = " ".join(paragraphs)  # 모든 문단을 하나의 문자열로 병합
    return text.strip()  # 양쪽 공백 제거


# Summarizer 클래스: KoBART 모델을 사용하여 텍스트 요약
class Summarizer:
    def __init__(self):
        """
        초기화 메서드
        - KoBART 모델과 토크나이저를 로드
        """
        self.tokenizer = PreTrainedTokenizerFast.from_pretrained(
            "jx7789/kobart_summary_v3"
        )  # KoBART 전용 토크나이저 로드
        self.model = BartForConditionalGeneration.from_pretrained(
            "jx7789/kobart_summary_v3"
        )  # KoBART 모델 로드

    def summarize_text(self, text):
        """
        텍스트 요약 메서드
        - 입력 텍스트를 전처리한 후 KoBART를 사용하여 요약
        """
        preprocessed_text = preprocess_text(text)  # 텍스트 전처리

        inputs = self.tokenizer(  # 텍스트를 KoBART 모델 입력 형식으로 변환
            preprocessed_text,
            return_tensors="pt",  # PyTorch 텐서 형식 반환
            max_length=1024,  # 입력 길이 제한
            truncation=True,  # 길이가 초과하면 자름
            padding=True,  # 필요한 경우 패딩 추가
        )

        with torch.no_grad():  # 추론 중 그래디언트 계산 방지
            summary_ids = self.model.generate(
                inputs["input_ids"],
                max_length=60,  # 출력 요약 최대 길이
                min_length=40,  # 출력 요약 최소 길이
                num_beams=6,  # 빔 서치 개수
                temperature=0.5,  # 텍스트 다양성 제어
                top_k=20,  # 확률 상위 20개 선택
                top_p=0.85,  # 누적 확률 상위 85% 선택
                repetition_penalty=2.5,  # 반복 페널티 적용
                length_penalty=0.8,  # 길이에 따른 페널티 적용
                do_sample=True,  # 샘플링 활성화
                early_stopping=True,  # 목표 조건 만족 시 출력 종료
            )

        summary = self.tokenizer.decode(
            summary_ids[0], skip_special_tokens=True
        )  # 요약 결과 디코딩
        return summary  # 요약 반환


# URL 처리 함수: 크롤링과 요약을 통합 수행
def process_url(url, crawler: Callable):
    """
    URL 처리 함수
    - 주어진 URL의 내용을 크롤링한 뒤 요약
    """
    result = crawler(url)  # 크롤링 수행

    if (
        result
        and "content" in result
        and result["content"] != "본문을 찾을 수 없습니다."
    ):  # 본문이 유효한 경우
        try:
            summarizer = Summarizer()  # Summarizer 인스턴스 생성
            summary = summarizer.summarize_text(result["content"])  # 본문 요약
            return {
                "title": result["title"],  # 제목
                "summary": summary,  # 요약 결과
                "tags": result.get("tags", []),  # 태그 (없으면 빈 리스트)
            }
        except Exception as e:
            return {"error": f"요약 중 오류 발생: {str(e)}"}  # 예외 발생 시 오류 반환
    else:
        return {
            "error": "크롤링된 내용이 없거나 본문을 찾을 수 없습니다."
        }  # 본문이 없거나 유효하지 않은 경우 오류 반환


# 메인 실행 코드
if __name__ == "__main__":
    """
    스크립트 실행 시 수행되는 메인 코드
    - 테스트 URL의 내용을 크롤링하고 요약
    """
    url = "https://velog.io/@lionloopy/%EC%BD%94%EB%93%9C%EB%A7%8C-%EC%9E%98-%EC%A7%9C%EB%A9%B4-%EB%90%9C%EB%8B%A4%EA%B3%A0-%EC%8B%A0%EC%9E%85%EC%A3%BC%EB%8B%88%EC%96%B4-%EA%B0%9C%EB%B0%9C%EC%9E%90%EA%B0%80-%EC%95%8C%EC%95%84%EC%95%BC-%ED%95%A0-100%EA%B0%80%EC%A7%80-%ED%95%84%EC%88%98-%EA%BF%80%ED%8C%81-1"  # 테스트 URL

    result = process_url(url, get_velog_content)  # URL 처리

    if "error" in result:
        print(result["error"])
    else:
        print("제목:", result["title"])  # 크롤링된 제목 출력
        print("\n요약 결과:")  # 요약 결과 출력
        print(result["summary"])
        if result["tags"]:  # 태그가 있는 경우 출력
            print("\n태그:", ", ".join(result["tags"]))
