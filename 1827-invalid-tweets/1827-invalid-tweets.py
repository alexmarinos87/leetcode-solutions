import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    mask = tweets["content"].str.len() > 15          # boolean mask
    return tweets.loc[mask, ["tweet_id"]]            # keep only the IDs
