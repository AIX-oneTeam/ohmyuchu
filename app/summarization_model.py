import torch
from transformers import PreTrainedTokenizerFast, BartForConditionalGeneration
from crawling_velog import get_velog_content


def preprocess_text(text):
    """텍스트 전처리"""
    first_paragraph = text.split("\n")[0]
    text = first_paragraph + ". " + text
    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
    text = " ".join(paragraphs)
    return text.strip()


class Summarizer:
    def __init__(self):
        self.tokenizer = PreTrainedTokenizerFast.from_pretrained(
            "digit82/kobart-summarization"
        )
        self.model = BartForConditionalGeneration.from_pretrained(
            "digit82/kobart-summarization"
        )

    def summarize_text(self, text):
        """핵심 내용 중심의 요약 함수"""
        preprocessed_text = preprocess_text(text)

        inputs = self.tokenizer(  # 여기를 수정했습니다
            preprocessed_text,
            return_tensors="pt",
            max_length=1024,
            truncation=True,
            padding=True,
        )

        with torch.no_grad():
            summary_ids = self.model.generate(
                inputs["input_ids"],
                max_length=36,
                min_length=15,
                num_beams=6,
                temperature=0.5,
                top_k=20,
                top_p=0.85,
                repetition_penalty=2.5,
                length_penalty=0.8,
                do_sample=True,
                early_stopping=True,
            )

        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary


def process_url(url, crawler: function):
    """URL을 받아서 크롤링과 요약을 처리하는 함수"""
    # 크롤링 실행
    result = crawler(url)

    if (
        result
        and "content" in result
        and result["content"] != "본문을 찾을 수 없습니다."
    ):
        try:
            summarizer = Summarizer()
            summary = summarizer.summarize_text(result["content"])
            return {
                "title": result["title"],
                "summary": summary,
                "tags": result.get("tags", []),
            }
        except Exception as e:
            return {"error": f"요약 중 오류 발생: {str(e)}"}
    else:
        return {"error": "크롤링된 내용이 없거나 본문을 찾을 수 없습니다."}


if __name__ == "__main__":
    # 테스트할 URL
    url = "https://velog.io/@nibble/2024%EB%85%84-%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%A5%BC-%EA%B7%B8%EB%A7%8C%EB%91%94-%EC%82%AC%EB%9E%8C%EC%9D%98-%ED%9A%8C%EA%B3%A0%EA%B8%80"

    result = process_url(url)

    if "error" in result:
        print(result["error"])
    else:
        print("제목:", result["title"])
        print("\n요약 결과:")
        print(result["summary"])
        if result["tags"]:
            print("\n태그:", ", ".join(result["tags"]))
