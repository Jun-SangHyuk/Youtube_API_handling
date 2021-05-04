from googleapiclient.discovery import build
import pandas as pd
import time

target_channels=['UCrvYntMt6mTIX94aIpX504g', 'UCSzcChLI2YC53oPLL8fz5Og', 'UCaQIf6kloCTi0Y0u7ahcPzg', 'UCy7C3ZPxW8rSZ6e6VaHHw0g', 'UCIDIwgx-vuTTKPAqscaD9KQ', # 게임
                 'UCl3Iufkr-Mq70QqmPx6SKIw', 'UCy4iNxlWZ5ZN-lTOuW8ijaA', 'UCzf0ZnoAKCX4io3DCPpPgEA', 'UC_nsseYlb6bSvVD2P7pGWkg', 'UCS9yGQhh0Q3WB7VUUkzUe7A', # 동물
                 'UCnqA97Ib0KRYbCz2CVVNv8w', 'UCiYtB2kLBTcnvODuzAB0_WQ', 'UCdZ2LqhKsjTIMPeVVhzs0Qw', 'UC9VXsiDfpZuq6YDL-7qZ2pw', 'UCNOfObVwhc2hXSf98cQ_sBg', # IT
                 'UCL6UtSBReI44RY6h4JWiqnQ', 'UCWoCbxeYaGNNAJh9YdW2Kdw', 'UCG2cxMiMh4qw0-k1Xa9ba_Q', 'UC874qBZw8UwIBnGWxc7D3Zg', 'UC7lt7JT1cAWQHQM1K9KfkxA', # 경제
                 'UCrvYntMt6mTIX94aIpX504g', 'UCMM32VnpPRPoQtgsAqGZrDQ', 'UCEfNSfpWPLILuklSjzoUzzw', 'UCQFAWXcuwAhZCCbjPF8jFRg', 'UCDdhy4Sc4So36HgTpoXUIOw'] # 영화 첫번째 겹침

api_obj = build('youtube', 'v3',
                developerKey='AIzaSyBgO1-g9efNyqSWCwdNzlf98tQSxHjTtYk')

pre_list = []
for i in target_channels:
    response = api_obj.channels().list(part='statistics', id=i).execute()
    if len(response) > 3:
        pre_list.append({"ch_id": response['items'][0]['id'],
                  "subscriver": response['items'][0]['statistics']['subscriberCount'],
                  "collecte_date": time.strftime("%y.%d.%m")})

results = pd.DataFrame(pre_list)
print(results)
results.to_csv('C:/projects/testcode/youtube/output/'+time.strftime("%y.%d.%m")+'subscrivercount.csv', index=False)

