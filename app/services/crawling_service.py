
# urlExamle
# 1. naver blog: https://blog.naver.com
# 2. brunch: https://brunch.co.kr
# 3. tistory: https://tistory.com
# 4. velog: https://velog.io
from crawling_brunch import get_brunch_content
from crawling_velog import get_velog_content
from summarization_model import process_url


def crawlingfromUrl(url: str):
    content = None
    title = None
    tags = None
    crawler = None

    if 'brunch' in url:
        crawler = get_brunch_content 
    if 'naver' in url:
        pass
    if 'tistory' in url:
        pass
    if 'velog' in url:
        crawler = get_velog_content

    return process_url(url, crawler)
    