api_key = "본인 키 입력"
from apiclient.discovery import build
youtube = build('youtube', 'v3', developerKey=api_key)

res=youtube.channels().list(id='UCkUq-s6z57uJFUFBvZIVTyg',
                            part='contentDetails').execute()
print(res)

ree = youtube.playlistItems().list(playlistId='UUkUq-s6z57uJFUFBvZIVTyg',
                                   part='snippet',
                                   maxResults=50).execute()


def get_channel_videos(channel_id):
    # get Uploads playlist id
    res = youtube.channels().list(id=channel_id,
                                  part='contentDetails').execute()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    videos = []
    next_page_token = None

    while 1:
        res = youtube.playlistItems().list(playlistId=playlist_id,
                                           part='snippet',
                                           maxResults=50,
                                           pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')

        if next_page_token is None:
            break

    return videos

videos = get_channel_videos('UCkUq-s6z57uJFUFBvZIVTyg')
print(len(videos))

for video in videos:
    print(video['snippet']['title'])

res = youtube.videos().list(id=videos[0]['snippet']['resourceId']['videoId'], part= 'statistics').execute()

print(res)


def get_videos_stats(video_ids):
    stats = []
    for i in range(0, len(video_ids), 50):
        res = youtube.videos().list(id=','.join(video_ids[i:i + 50]),
                                    part='statistics').execute()
        stats += res['items']

    return stats


video_ids = list(map(lambda x:x['snippet']['resourceId']['videoId'], videos))
stats = get_videos_stats(video_ids)
print(len(stats))
most_disliked = sorted(stats, key=lambda x:int(x['statistics']['dislikeCount']), reverse=True)
for video in most_disliked:
    print(video['id'], video['statistics']['dislikeCount'])
