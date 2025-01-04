import praw

def fetch_reddit_post():
    try:
        reddit = praw.Reddit(
        client_id="",
        client_secret="",
        user_agent="",
        )

        input_url = input("사용자의 URL 을 입력하세요: ").strip()
        
        # 사용자 이름 추출
        if "reddit.com" in input_url:
            username = input_url.rstrip('/').split('/')[-1]
      
        user = reddit.redditor(username)

        print(f"요청하신 사용자: {username}")
        
        # 최신 게시물 가져오기
        posts = list(user.submissions.new(limit=1))  # 게시물 리스트로 변환

        if not posts:
            print("이 사용자는 게시물이 없습니다.")
            return

        for submission in posts:
            print("\n게시물을 찾았습니다::")
            print(f"제목: {submission.title}")
            print(f"내용: {submission.selftext}")

    except praw.exceptions.RedditAPIException as api_error:
        print(f"Reddit API error: {api_error}")
    except praw.exceptions.Forbidden:
        print("이 사용자의 게시물에 접근할 수 없습니다 (403).")
    except Exception as e:
        print(f"오류가 발생했습니다.: {type(e).__name__}: {str(e)}")

if __name__ == "__main__":
    fetch_reddit_post()
