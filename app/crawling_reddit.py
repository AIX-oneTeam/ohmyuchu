import praw

def get_reddit_content(url: str) -> dict:
    """
    주어진 Reddit 게시글 URL에서 제목, 내용, 태그를 추출하는 함수.

    Args:
        url (str): Reddit 게시글 URL

    Returns:
        dict: 게시글의 제목, 내용, 태그
    """
    try:
        # Reddit API 초기화
        reddit = praw.Reddit(
            client_id="mCpW5hFdCqnojb9XnVVywg",
            client_secret="5pdCX0laJzwXs5a87q8souH2lAkMxg",
            user_agent="script:TestApp:v1.0",
        )

        # 게시글 ID 추출
        if "reddit.com" in url:
            post_id = url.rstrip('/').split('/')[6]  # URL의 6번째 요소가 post_id
        else:
            return {
                "title": "유효하지 않은 Reddit URL입니다.",
                "content": "",
                "tags": []
            }

        # 게시글 객체 가져오기
        submission = reddit.submission(id=post_id)

        # 결과 반환
        return {
            "title": submission.title,
            "content": submission.selftext,
            "tags": [tag.name for tag in submission.link_flair_richtext] if submission.link_flair_richtext else []
        }

    except praw.exceptions.RedditAPIException as api_error:
        return {
            "title": "Reddit API 오류 발생",
            "content": str(api_error),
            "tags": []
        }
    except Exception as e:
        return {
            "title": "오류 발생",
            "content": f"{type(e).__name__}: {str(e)}",
            "tags": []
        }

# 직접 실행 시 테스트 코드
if __name__ == "__main__":
    test_url = "https://www.reddit.com/user/gomting_02/comments/1hse5db/2025%EB%85%84_1%EC%9B%94_3%EC%9D%BC_%EA%B8%88%EC%9A%94%EC%9D%BC/"
    result = get_reddit_content(test_url)
    print(result)
