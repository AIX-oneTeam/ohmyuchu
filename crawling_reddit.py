import praw

# Reddit 게시물 가져오기 및 감정 분석
def get_user_posts_and_analyze():
    try:
        # Reddit 인스턴스 생성
        reddit = praw.Reddit(
           client_id="mCpW5hFdCqnojb9XnVVywg",
            client_secret="5pdCX0laJzwXs5a87q8souH2lAkMxg",
            user_agent="script:TestApp:v1.0",
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
            print("-" * 50)      
    
    except Exception as e:
        print(f"Error occurred: {type(e).__name__}: {str(e)}")
        print(f"Full error details: {str(e)}")


#예시 실행 코드.
if __name__ == " main":
    get_user_posts_and_analyze()

    