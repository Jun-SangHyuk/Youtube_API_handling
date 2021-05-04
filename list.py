from apiclient.discovery import build
from datetime import datetime
import pandas
from googleapiclient.discovery import build
import comment

comments = list()
api_obj = build('youtube', 'v3',
                developerKey='AIzaSyBgO1-g9efNyqSWCwdNzlf98tQSxHjTtYk')
response = api_obj.videos().list(part='snippet', chart='mostPopular',
                                 regionCode='KR', maxResults=50).execute()

popular_list = []
for i in response['items']:
    popular_list.append(i['id'])

print(popular_list)

for i in range(len(popular_list) - 48):
    ddd = comment.videoComment(popular_list[i])
    ddd.makelist()
    ddd.makedf()
