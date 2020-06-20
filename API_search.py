api_key = "본인 키 "
from apiclient.discovery import build
from datetime import datetime
import pandas as pd
# GET https://www.googleapis.com/youtube/v3/channels

youtube = build('youtube', 'v3', developerKey=api_key)

#시간설정
start_time = datetime(year=2019, month=8, day=1).strftime('%Y-%m-%dT%H:%M:%SZ')
end_time = datetime(year=2019, month=8, day=19).strftime('%Y-%m-%dT%H:%M:%SZ')

#유튜브 채널
# res = youtube.channels().list(part='snippet',
#                               categoryId=15,
#                               forUsername='haha ha',
#                               id='UCOp66Vup07X0YziXaaxqs2A',
#                               managedByMe=False,
#                               mine=False,
#                               maxResults=50
#                               ).execute
#유튜브 서치
res = youtube.search().list(part='snippet',
                            q='haha ha',
                            maxResults=50,
                            type='video',
                            publishedAfter=start_time,
                            publishedBefore=end_time
                            ).execute()
# print(res)
# for item in res['items']:
#     print(item['snippet']['channelTitle'])

def search_csv(res):
    result = []
    for item in res['items']:
        item_list = []
        item_list.append(item['snippet']['publishedAt'])
        item_list.append(item['snippet']['channelTitle'])
        item_list.append(item['snippet']['channelId'])
        item_list.append(item['snippet']['title'])
        item_list.append(item['snippet']['thumbnails']['high']['url'])
        item_list.append(item['snippet']['description'])
        item_list.append(item['snippet']['liveBroadcastContent'])
        result.append(item_list)
    return pd.DataFrame(result)

search_csv(res).to_csv('API_search.csv', encoding='utf-8-sig', index=False)


