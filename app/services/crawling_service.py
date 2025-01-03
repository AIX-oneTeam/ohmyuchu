
# urlExamle
# 1. naver blog: https://blog.naver.com
# 2. brunch: https://brunch.co.kr
# 3. tistory: https://tistory.com
# 4. velog: https://velog.io
from app import crawling_brunch, crawling_velog
from app.summarization_model import process_url


async def crawlingfromUrl(url: str):
    content = None
    title = None
    tags = None
    crawler = None

    if 'brunch' in url:
        crawler = crawling_brunch
    if 'naver' in url:
        pass
    if 'tistory' in url:
        pass
    if 'velog' in url:
        crawler = crawling_velog

    title, contents, tags = process_url(url, crawler)
    print(title, contents, tags)
    