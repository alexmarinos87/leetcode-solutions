import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    """
    Return a DataFrame with the tweet_id of tweets whose content
    length is strictly greater than 15 characters.
    """
    mask = tweets["content"].str.len() > 15          # boolean mask
    return tweets.loc[mask, ["tweet_id"]]            # keep only the IDs
