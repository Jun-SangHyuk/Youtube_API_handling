from apiclient.discovery import build
from datetime import datetime
import pandas
from googleapiclient.discovery import build


class videoComment:
    def __init__(self, vid):
        self.vid = vid
        self.api_obj = build('youtube', 'v3',
                             developerKey='AIzaSyBazlb6h9bz0zTTJ3EnrAmVhf5CjA9Azvs')
        self.response = self.api_obj.commentThreads().list(
            part='snippet,replies', videoId=self.vid, maxResults=100).execute()
        self.comments = list()

    def makelist(self):
        # self.response = api_obj.commentThreads().list(part='snippet,replies', videoId=vid, maxResults=100).execute()
        print('doing make list '+self.vid)
        while self.response:
            for item in self.response['items']:
                comment = item['snippet']['topLevelComment']['snippet']
                self.comments.append(
                    [comment['textDisplay'], comment['authorDisplayName'],
                     comment['publishedAt'], comment['likeCount'], self.vid])

                if item['snippet']['totalReplyCount'] > 0:
                    for reply_item in item['replies']['comments']:
                        reply = reply_item['snippet']
                        self.comments.append(
                            [reply['textDisplay'], reply['authorDisplayName'],
                             reply['publishedAt'], reply['likeCount'],
                             self.vid])
            if 'nextPageToken' in self.response:
                self.response = self.api_obj.commentThreads().list(
                    part='snippet,replies', videoId=self.vid,
                    pageToken=self.response['nextPageToken'],
                    maxResults=100).execute()
            else:
                break

    def makedf(self):
        print('doing make df ' + self.vid)
        from sqlalchemy import create_engine
        import time
        df = pandas.DataFrame(self.comments,
                              columns=['comment', 'author', 'date', 'num_likes',
                                       'vid'])
        df = df.assign(collecte_date=time.strftime("%y.%d.%m"))
        df = df.sort_values(by='num_likes', axis=0, ascending=False)
        # engine = create_engine(
        #     "postgresql://postgres:cslee@localhost:5432/postgres")
        # df.to_sql(name="youtube_comments_test2", con=engine,
        #           if_exists='append', chunksize=None,
        #           method='multi', index=False)
        df.to_csv()