api_key = "본인 키 입력"
from apiclient.discovery import build
from datetime import datetime

# GET https://www.googleapis.com/youtube/v3/channels

youtube = build('youtube', 'v3', developerKey=api_key)
start_time = datetime(year=2019, month=8, day=1).strftime('%Y-%m-%dT%H:%M:%SZ')
end_time = datetime(year=2019, month=8, day=19).strftime('%Y-%m-%dT%H:%M:%SZ')


# res = youtube.channels().list(part='snippet',
#                               # categoryId=15,
#                               # forUsername='haha ha',
#                               id='UCOp66Vup07X0YziXaaxqs2A',
#                               # managedByMe=False,
#                               # mine=False
#                               maxResults=50
#                               ).execute
res = youtube.search().list(part='snippet',
                            q='생활코딩',
                            maxResults=50,
                            type='video',
                            publishedAfter=start_time,
                            publishedBefore=end_time
                            ).execute()
print(res)
# for item in res['items']:
#     print(item['snippet']['channelTitle'])
