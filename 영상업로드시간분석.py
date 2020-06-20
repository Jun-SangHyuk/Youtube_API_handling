from apiclient.discovery import build
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

api_key = "본인 키 "
youtube = build('youtube', 'v3', developerKey=api_key)

def get_channel(channel_name):
    return youtube.search().list(q=channel_name, type='channel', part='id,snippet').execute()['items'][0]


def get_videos(channel_id, part='id,snippet', limit=10):
    res = youtube.channels().list(id=channel_id,
                                  part='contentDetails').execute()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    videos = []
    next_page_token = None

    while 1:
        res = youtube.playlistItems().list(playlistId=playlist_id,
                                           part=part,
                                           maxResults=min(limit, 50),
                                           pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')

        if next_page_token is None or len(videos) >= limit:
            break

    return videos


def parse_publish_timestamp(video):
    return (datetime.strptime(video['snippet']['publishedAt'], "%Y-%m-%dT%H:%M:%S.000Z")
            + timedelta(hours=5, minutes=30))

channel_id = get_channel('대도서관')['id']['channelId']
videos = get_videos(channel_id, limit=500)
publish_timestamps = [parse_publish_timestamp(video) for video in videos]
publish_times = [t.hour + t.minute/60 for t in publish_timestamps]


path = 'C:/Users/user/AppData/Local/Microsoft/Windows/Fonts/KoPub Dotum Bold.ttf'
fontprop = fm.FontProperties(fname=path)
plt.hist(publish_times, bins=24)
plt.xlabel('시간', fontsize=5, fontproperties= fontprop)
plt.ylabel('업로드 수', fontsize=5, fontproperties= fontprop)
plt.title('대도서관', fontproperties= fontprop)
plt.xticks(range(24))
plt.show()
