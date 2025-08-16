from googleapiclient.discovery import build #to build video or extract youtube video
import pandas as pd #our data engineering essentials, u know for cleaning extractic etc
from sqlalchemy import create_engine #for DB after getting data we will upload to PostgreSQL
#1 extract
API_KEY = "AIzaSyDd4ld9QmdUSh6QagyDLbaVjV78UA1gWXc"
YOUTUBE = build("youtube", "v3", developerKey=API_KEY)

def fetch_trending_videos(region="US", max_results=10):
    request = YOUTUBE.videos().list(
        part="snippet,statistics",
        chart="mostPopular",
        regionCode=region,
        maxResults=max_results
    )
    response = request.execute()

    #parsing video "response" into list
    videos = []
    for item in response["items"]:
        videos.append({
            "video_id": item["id"],
            "title": item["snippet"]["title"],
            "channel_title": item["snippet"]["channelTitle"],
            "published_at": item["snippet"]["publishedAt"],
            "views": int(item["statistics"].get("viewCount", 0)),
            "likes": int(item["statistics"].get("likeCount", 0)),
            "comments": int(item["statistics"].get("commentCount",0))
        })
    return pd.DataFrame(videos)
#checking if data correct
df = fetch_trending_videos(region="US", max_results=20)
#print(df.head())

#2 Transform
df["published_at"] = pd.to_datetime(df["published_at"]) #properly use correct format for date and time (pandas)
df = df[df["views"] > 0] #take video greater than 0 only
#print(df["title"])


#3 Load (PostgreSQL)
engine = create_engine("postgresql+psycopg2://postgres:%40Alifasyraf1@localhost:5432/youtube_db")
#save dataframe into PostgreSQL
df.to_sql("trending_videos", engine, schema="public", if_exists="replace", index=False)
print("Data loaded into PostgreSQL sucessfully!")