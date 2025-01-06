from pymongo import MongoClient

# MongoDB 연결 설정
mongoDB_url: str = "mongodb+srv://yesol:yesol9639@test.9r2s8.mongodb.net/"
database_name: str = "test"
# mongoDB_url: str = "mongodb://192.168.0.141:27017"
# database_name: str = "ohmyuchu"

client = MongoClient(mongoDB_url)  # 적절한 MongoDB URI로 교체
db = client[database_name]  # 데이터베이스 이름
songs = db['songs']  # 컬렉션 이름

# 저장할 데이터
song_data_list = [{
    "title": "꺼져 줄게 잘 살아",
    "artist": "지나",
    "src": "https://www.youtube.com/embed/2eL3lKPVq-0?si=VR6ixLlQ8xNF4nVA",
    "emotion": "분노",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "Look What You Made Me Do",
    "artist": "Taylor Swift",
    "src": "https://www.youtube.com/embed/3tmd-ClpJxA?si=hMqzLiQKqdJPWaFk",
    "emotion": "분노",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "Press",
    "artist": "Cardi B",
    "src": "https://www.youtube.com/embed/-IdnRv04IZc?si=nDFqH8Xqa7at5V82",
    "emotion": "분노",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "만만하니",
    "artist": "유키스",
    "src": "https://www.youtube.com/embed/EBBCpTO0hyc?si=SG1PGplP7zR32MWy",
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
    "title": "Tubular Bells",
    "artist": "Mike Oldfield",
    "src": "https://www.youtube.com/embed/FN6jIvKiYOs?si=zNHZsCRvec-NaeZ_",
    "emotion": "공포",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "A Nightmare on Elm Street Theme",
    "artist": "Charles Bernstein",
    "src": "https://www.youtube.com/embed/HZSnwJOQp0A?si=HcC1EfvKPaZrZccA",
    "emotion": "공포",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "Main Title (The Shining) ",
    "artist": "Wendy Carlos & Rachel Elkind",
    "src": "https://www.youtube.com/embed/pylfy_L6Bjs?si=qLvJ61D7s4b01KD9",
    "emotion": "공포",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "bury a friend",
    "artist": "Billie Eilish",
    "src": "https://www.youtube.com/embed/HUHC9tYz8ik?si=798PkbJ0mtRklL98",
    "emotion": "공포",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "Ain’t shit",
    "artist": "Doja Cat",
    "src": "https://www.youtube.com/embed/13MvatpPQv4?si=Bv_15_1Z2rSFFmd2",
    "emotion": "혐오",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "I Hate Everything About You",
    "artist": "Three Days Grace",
    "src": "https://www.youtube.com/embed/d8ekz_CSBVg?si=-0lBLNnmE3-5RbcU",
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
    "title": "Creep",
    "artist": "Radiohead",
    "src": "https://www.youtube.com/embed/zFYEYRcjK2g?si=UVhJoUglQBmHTV3K",
    "emotion": "혐오",
    "play_count": 0,
    "like_count": 0,
    "dislike_count": 0
},
{
    "title": "Since U Been Gone",
    "artist": "Kelly Clarkson",
    "src": "https://www.youtube.com/embed/R7UrFYvl5TE?si=r-h3acERA64RKctF",
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
# 데이터 삽입
result = songs.insert_many(song_data_list)

# 삽입 결과 확인
print(f"Inserted document ID: {result.inserted_ids}")
