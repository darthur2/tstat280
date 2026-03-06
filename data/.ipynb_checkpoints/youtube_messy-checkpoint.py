import pandas as pd
from random import randint

yt = pd.read_csv("../data/youtube.csv")
yt_messy = yt

yt_messy["category"] = yt_messy["category"].map(
    lambda x: x + "  " if randint(a=1, b=4) == 1
    else x.lower() if randint(a=1, b=3) == 1
    else " " + x[0:4] + " " if randint(a=1, b=2) == 1
    else x
)

yt_messy["language"] = yt_messy.apply(
    lambda row: row["language"] + "," + row["region"] if randint(a=1, b=3) == 1
    else row["language"] + "; " + row["region"] if randint(a=1, b=2) == 1
    else row["language"],
    axis = 1
)

yt_messy["region"] = yt_messy["region"].map(
    lambda x: x.lower() if randint(a=1, b=2) == 1
    else x
)

yt_messy["duration_sec"] = yt_messy["duration_sec"].map(
    lambda x: str(x) + " sec" if randint(a=1, b=4) == 1
    else str(x) + " seconds" if randint(a=1, b=3) == 1
    else str(x/60) + " min" if randint(a=1, b=2) == 1
    else str(x)
)

yt_messy["views"] = yt_messy["views"].map(
    lambda x: x if randint(a=1, b=2000) > 10
    else None
)

yt_messy["likes"] = yt_messy["likes"].map(
    lambda x: str(x)
)

yt_messy["comments_shares"] = yt_messy.apply(
    lambda row: str(row["comments"]) + ";" + str(row["shares"]),
    axis = 1
)

yt_messy["sentiment_score"] = yt_messy["sentiment_score"].map(
    lambda x: x if randint(a=1, b=2000) > 10
    else x*100
)

yt_messy = yt_messy[["timestamp", "video_id", "category", "language", "region", "duration_sec",
                     "views", "likes", "comments_shares", "sentiment_score", "ads_enabled"]]

yt_messy.info()