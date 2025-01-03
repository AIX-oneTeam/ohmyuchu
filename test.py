import praw

def get_user_posts():
    try:
        # Reddit 인스턴스 생성
        reddit = praw.Reddit(
            client_id="",
            client_secret="",
            user_agent="",
            check_for_async=False
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

    except Exception as e:
        print(f"Error occurred: {type(e).__name__}: {str(e)}")
        print(f"Full error details: {str(e)}")

if __name__ == "__main__":
    get_user_posts()