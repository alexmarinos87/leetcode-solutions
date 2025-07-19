import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
        # Identify rows where author_id == viewer_id
    self_views = views['author_id'] == views['viewer_id']

    # Keep just those rows, pull the author_id column,
    #    drop duplicates, rename, and sort as required
    return (
        views.loc[self_views, ['author_id']]      # row filter + column slice
             .drop_duplicates()                   # one row per author
             .rename(columns={'author_id': 'id'}) # match expected header
             .sort_values('id', ignore_index=True)
    )
