
# urlExamle
# 1. naver blog: https://blog.naver.com
# 2. brunch: https://brunch.co.kr
# 3. tistory: https://tistory.com
# 4. velog: https://velog.io
from crawling_naver import get_blog_content
from crawling_brunch import get_brunch_content
from crawling_velog import get_velog_content
from summarization_model import process_url
from crawling_tistory import get_tistory_content
from crawling_reddit import get_reddit_content
from crawling_x import get_x_content

def crawlingfromUrl(url: str):
    content = None
    title = None
    tags = None
    crawler = None

    if 'brunch' in url:
        crawler = get_brunch_content 
    if 'naver' in url:
        crawler = get_blog_content
    if 'tistory' in url:
        crawler = get_tistory_content
    if 'velog' in url:
        crawler = get_velog_content
    if 'reddit' in url:
        crawler = get_reddit_content 
    if 'x' in url:
        crawler = get_x_content    


    return process_url(url, crawler)
    