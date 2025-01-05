def get_song_data(emotion:str) :
    # 감정에 해당하는 노래 중에서 랜덤으로 하나 선택
    random_song = songs_collection.aggregate([
        {"$match": {"emotion": emotion}},  # 감정에 맞는 노래만 필터링
        {"$sample": {"size": 1}}  # 랜덤으로 1개의 노래 선택
    ])
    
    # 결과가 있으면 반환
    song = list(random_song)
    
    if song:
        # 노래 정보 반환
        selected_song = song[0]
        song_data = {
            "title": selected_song["title"],
            "artist": selected_song["artist"],
            "src": selected_song["src"]
        }

        songs_collection.update_one(
            {"title": selected_song["title"]},
            {"$inc": {"like_count": 1}}
        )

        analysis_collection.update_one(
            {"title": selected_song["title"]},
            {"$inc": {"total_play_count": 1,
                      f"emotion_summary.{emotion}": 1}}
        )
        return song_data

    else:
        return "알 수 없는 감정입니다."

