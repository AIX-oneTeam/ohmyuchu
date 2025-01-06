async def get_song_data(emotion:str, songs_collection, analysis_collection) :

    # 감정에 해당하는 노래 중에서 랜덤으로 하나 선택
    random_song_list = await songs_collection.aggregate([
        {"$match": {"emotion": emotion}},  # 감정에 맞는 노래만 필터링
        {"$sample": {"size": 1}}  # 랜덤으로 1개의 노래 선택
    ]).to_list(length=1)

    if not random_song_list:
        return "알 수 없는 감정입니다."
    
    selected_song = random_song_list[0]
    song_data = {
        "title": selected_song["title"],
        "artist": selected_song["artist"],
        "src": selected_song["src"]
    }

    await songs_collection.update_one(
        {"title": selected_song["title"]},
        {"$inc": {"like_count": 1}}
    )

    await analysis_collection.update_one(
        {"title": selected_song["title"]},
        {"$inc": {"total_play_count": 1,
                    f"emotion_summary.{emotion}": 1}}
    )
    return song_data

