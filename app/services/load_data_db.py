from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 로드
load_dotenv()

from pymongo import MongoClient
from datetime import datetime
mongoDB = os.getenv("mongoDB")

# MongoDB 연결 설정
mongoDB_url: str = mongoDB
database_name: str = "test"

client = MongoClient(mongoDB_url)  # MongoDB URI로 교체
db = client[database_name]  # 데이터베이스 이름

# songs 데이터 삽입 저장할 데이터
songs = db['songs']  # 컬렉션 이름
song_data_list = [{
    "title": "아주 NICE",
    "artist": "세븐틴(SEVENTEEN)",
    "src": "https://www.youtube.com/embed/J-wFp43XOrA?si=2Wh5EZGDy_JH5sKM",
    "emotion": "기쁨",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "Festival",
    "artist": "엄정화",
    "src": "https://www.youtube.com/embed/aymUZ29UeLQ?si=3RPZN4zWokKKJr0M",
    "emotion": "기쁨",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "HAPPY",
    "artist": "데이식스(DAY-6)",
    "src": "https://www.youtube.com/embed/2o1zdX72400?si=juBPGQyOAEqUdle8",
    "emotion": "기쁨",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "That That",
    "artist": "싸이(PSY)",
    "src": "https://www.youtube.com/embed/8dJyRm2jJ-U?si=B0BFj5rTjj27a45F",
    "emotion": "기쁨",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "Happy Things",
    "artist": "제이래빗(J Rabbit)",
    "src": "https://www.youtube.com/embed/fhs55HEl-Gc?si=u754nAI5F15_WaB0",
    "emotion": "기쁨",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},{
    "title": "무릎(Knees)",
    "artist": "아이유(IU)",
    "src": "https://www.youtube.com/embed/SfeaTW4bcAw?si=EuXQK9oSzuXcOudS",
    "emotion": "슬픔",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "그렇게 살아가는 것(So life goes on)",
    "artist": "허회경(Heo Hoy Kyung)",
    "src": "https://www.youtube.com/embed/1Qtr8TznwNI?si=6XVKPz_k8oXAH3IQ",
    "emotion": "슬픔",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "서울의 잠 못 이루는 밤(Feat.이수현)",
    "artist": "십센치(10CM)",
    "src": "https://www.youtube.com/embed/KK-ffKikwBw?si=gJ--DmLX2_ayF1ws",
    "emotion": "슬픔",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "By Lake Surprise (Scaled Down Version)",
    "artist": "Peter Sandberg",
    "src": "https://www.youtube.com/embed/SfeaTW4bcAw?si=EuXQK9oSzuXcOudS",
    "emotion": "슬픔",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "무릎(Knees)",
    "artist": "아이유(IU)",
    "src": "https://www.youtube.com/embed/r80BtiDen6Q?si=WbPaXBXeZA2XyCF7",
    "emotion": "슬픔",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "이사(Moving)",
    "artist": "크르르(Krr)",
    "src": "https://www.youtube.com/embed/XZoP7SQauQg?si=fZxG5xcrkd1ueLr9",
    "emotion": "슬픔",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},{
    "title": "니가 왜 거기서 나와",
    "artist": "영탁",
    "src": "https://www.youtube.com/embed/88a2RgUjRKk?si=OcNRAUMYAtjz6lUs",
    "emotion": "놀람",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},{
    "title": "어머나",
    "artist": "장윤정",
    "src": "https://www.youtube.com/embed/1g5BXEcv5zQ?si=L-lrN9lu_1Jx8Jpc",
    "emotion": "놀람",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},{
    "title": "SHOCK",
    "artist": "비스트(BEAST)",
    "src": "https://www.youtube.com/embed/JXxGo1MvNls?si=vKDy0S9u6KqCqieN",
    "emotion": "놀람",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},{
    "title": "Uh-Oh",
    "artist": "(여자)아이들",
    "src": "https://www.youtube.com/embed/I66oFXdf0KU?si=tZA5Z8bWOqxWfUG4",
    "emotion": "놀람",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},{
    "title": "How You Like That",
    "artist": "블랙핑크(BLACKPINK)",
    "src": "https://www.youtube.com/embed/32si5cfrCNc?si=NUS6_uCsBJlfZCnl",
    "emotion": "놀람",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},{
    "title": "꺼져 줄게 잘 살아",
    "artist": "지나",
    "src": "https://www.youtube.com/embed/2eL3lKPVq-0?si=VR6ixLlQ8xNF4nVA",
    "emotion": "분노",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "very good",
    "artist": "블락비",
    "src": "https://www.youtube.com/embed/kJGcO5Une-g?si=iiu5IGG6eqfIVKDx",
    "emotion": "분노",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "Sixth Sense",
    "artist": "브라운아이드걸스",
    "src": "https://www.youtube.com/embed/pIqkDBsSJOw?si=VKGlh6GzNX1VCE5M",
    "emotion": "분노",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "미친거니",
    "artist": "송지은",
    "src": "https://www.youtube.com/embed/n1TLaZp1i8E?si=jwnf8O-hWcgEn_Rq",
    "emotion": "분노",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "왜",
    "artist": "동방신기",
    "src": "https://www.youtube.com/embed/djJb5iSL0Do?si=ZsuSzxdRipfH6tQv",
    "emotion": "분노",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "HALLOWEEN Theme",
    "artist": "John Carpenter ",
    "src": "https://www.youtube.com/embed/gqVyois9mp4?si=N7W14mFBA1q9ZvM5",
    "emotion": "공포",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "망향",
    "artist": "자우림",
    "src": "https://www.youtube.com/embed/pilr-XugoHA?si=b1wuKyQ31AbDniWo",
    "emotion": "공포",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "발레리노",
    "artist": "리쌍",
    "src": "https://www.youtube.com/embed/G3qS8dD4kOk?si=humJO-fnHcOeWNBs",
    "emotion": "공포",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "피해망상pt.1 ",
    "artist": "에픽하이",
    "src": "https://www.youtube.com/embed/Jj2YOsFVuHM?si=LUUNmHy_ZZY04PJd",
    "emotion": "공포",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "피행망상 pt.3 (With TBNY)",
    "artist": "에픽하이",
    "src": "https://www.youtube.com/embed/wcSX4hs1bBM?si=X4-V4I7VYbdLqpp1",
    "emotion": "공포",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "손대지마",
    "artist": "에일리",
    "src": "https://www.youtube.com/embed/5cnjdPHDZ0k?si=iJqUvmg1YXwd1NIb",
    "emotion": "혐오",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "GO AWAY",
    "artist": "2NE1",
    "src": "https://www.youtube.com/embed/3yW13T2sfKg?si=yG8vIrT8U_0cEAR_",
    "emotion": "혐오",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "toxic till the end ",
    "artist": "ROSÉ",
    "src": "https://www.youtube.com/embed/eA0lHNZ1KCA?si=ScBkMSbD2EmNy0nl",
    "emotion": "혐오",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "Fxxked Up",
    "artist": "전소미 ",
    "src": "https://www.youtube.com/embed/yeCJ_MjsTYo?si=LZG8cqHAnFohY8tI",
    "emotion": "혐오",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "꺼져",
    "artist": "형돈이와 대준이",
    "src": "https://www.youtube.com/embed/792jeZ08h94?si=8an62XCBuq0fT1uK",
    "emotion": "혐오",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "별일 없이 산다",
    "artist": "장기하와 얼굴들",
    "src": "https://www.youtube.com/embed/CfXVsHNETq0?si=kbnkC4zfO2wBkfw_",
    "emotion": "중립",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "골목길",
    "artist": "양동근",
    "src": "https://www.youtube.com/embed/3zr4HJHIWpU?si=hWvAgzm2EqhguJne",
    "emotion": "중립",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "싸구려 커피",
    "artist": "장기하와 얼굴들",
    "src": "https://www.youtube.com/embed/bL-ueHzY2yM?si=5-tzXy93PwwjgC5n",
    "emotion": "중립",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "봄에 내기엔 늦었고 여름에 내기엔 좀 이른 노래",
    "artist": "형돈이와 대준이",
    "src": "https://www.youtube.com/embed/rB7B8YF1ZrQ?si=MbvjNFf_rpRBi0bI",
    "emotion": "중립",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "부럽지가 않어",
    "artist": "장기하",
    "src": "https://www.youtube.com/embed/SzyB2xBqkps?si=caUkGQ9bhhxRjw0q",
    "emotion": "중립",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
}

]
# #데이터 삽입
# result = songs.insert_many(song_data_list)

# # 삽입 결과 확인
# print(f"Inserted document ID: {result.inserted_ids}")


##############

# comment
comment = db['comment']  # 컬렉션 이름

# 저장할 데이터
message_data_list = [
{
"emotion": "기쁨",
"comment": [
"오늘은 기쁜 하루를 보내셨군요! 이런 날들이 계속해서 많아지길 바랄게요. 내일도 활짝 웃는 하루가 되길 응원합니다!",
"환하게 웃는 당신의 모습이 상상돼요. 오늘의 기쁨을 마음속 깊이 간직하시고, 더 많은 행복이 찾아오길 바랍니다!",
"행복한 하루를 보내셨다니 정말 다행이에요! 그 기쁨이 주변 사람들에게도 전달되었을 것 같아요. 내일도 좋은 일이 가득하길!"
    ]
},
{
"emotion": "슬픔",
"comment": [
"오늘은 슬픈 하루를 보내셨군요. 괜찮습니다, 누구에게나 이런 날이 있기 마련이에요. 잠시 쉬면서 마음을 다독여보세요. 곧 행복이 다시 찾아올 거예요!",
"마음이 힘들 땐 눈을 감고 깊게 숨을 쉬어보세요. 따뜻한 차 한 잔이나 조용한 음악도 당신에게 작은 위로가 될 거예요.",
"오늘 느꼈던 슬픔이 당신을 더 강하게 만들어 줄 거예요. 괜찮아요, 당신은 혼자가 아니에요. 곁에 있는 사람들이 당신을 응원하고 있어요."
    ]
},
{
"emotion": "놀람",
"comment": [
"오늘은 많이 놀란 하루를 보내셨군요. 깜짝 놀랐던 그 순간이 지금은 새로운 배움이나 즐거운 추억으로 남았길 바랄게요!",
"놀라운 하루를 보내셨다니 정말 흥미로웠겠어요. 예상치 못한 순간들이 때로는 삶을 더욱 풍성하게 만들어 주기도 하죠!",
"놀랐던 그 순간이 언젠가 웃으면서 떠올릴 수 있는 일이 되길 바라요. 오늘 하루도 당신에게 소중한 경험으로 남았길!"
    ]
},
{
"emotion": "분노",
"comment": [
"오늘은 많이 화가 난 하루를 보내셨군요. 화를 느낄 때는 잠시 숨을 고르고, 차분히 생각을 정리하는 것도 도움이 될 거예요. 내일은 더 평온한 하루가 되길 바라요.",
"화가 났던 이유를 스스로 이해하고, 그 감정을 흘려보내는 것도 중요해요. 당신의 평온함이 무엇보다 소중하니까요.",
"화난 감정이 오래 남지 않도록 가벼운 산책이나 좋아하는 활동으로 마음을 달래보세요. 내일은 더 긍정적인 에너지가 가득하길 바랍니다."
    ]
},
{
"emotion": "공포",
"comment": [
"오늘은 두려움을 느낀 하루였던 것 같아요. 괜찮아요, 당신은 생각보다 훨씬 강한 사람입니다. 걱정되는 일이 있다면 믿을 수 있는 사람과 함께 나누어보세요.",
"두려운 순간이 있었지만, 당신은 그걸 이겨냈어요. 앞으로도 그런 순간마다 스스로를 믿고 나아가길 바라요.",
"마음의 평온을 찾기 위해 잠시 모든 것을 내려놓고 자신을 위로하는 시간을 가져보세요. 당신은 충분히 해낼 수 있어요!"
    ]
},
{
"emotion": "혐오",
"comment": [
"오늘은 불쾌한 감정을 느끼셨군요. 이런 순간은 누구에게나 찾아오지만, 너무 오래 붙잡아 두지 말고 마음을 편하게 해줄 일을 찾아보세요. 당신의 하루는 더 소중하니까요.",
"불편했던 일이 있었다면, 그것이 당신의 하루를 전부 정의하지는 못해요. 좋은 일이 더 많을 수 있도록 마음을 열어보세요.",
"기분이 상했던 순간을 내려놓고, 당신을 행복하게 해줄 무언가에 집중해보세요. 내일은 더 빛나는 하루가 될 거예요."
        ]
        },
{
"emotion": "중립",
 "comment": [
"오늘은 감정적으로 특별한 일이 없었던 하루였군요. 평범한 날도 가끔은 소중합니다. 내일은 더 흥미롭고 즐거운 일이 가득하길 바라요!",
"감정의 파도가 잔잔한 하루를 보냈군요. 이런 날엔 스스로에게 조금 더 여유를 주고 작은 행복을 찾아보세요.",
"평범한 하루 속에서도 감사한 일들을 떠올려보세요. 오늘 하루도 당신의 소중한 삶의 일부니까요!"
    ]
}
]

# # # # # 데이터 삽입
# result = comment.insert_many(message_data_list)

# # # 삽입 결과 확인
# print(f"Inserted document ID: {result.inserted_ids}")
