import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    """
    Return all (actor_id, director_id) pairs that appear together
    at least three times in the ActorDirector table.

    Parameters
    ----------
    actor_director : pd.DataFrame
        Columns:
        - actor_id    : int
        - director_id : int
        - timestamp   : int  (unique, not needed for the query)

    Returns
    -------
    pd.DataFrame
        Columns:
        - actor_id
        - director_id
        Each row is a pair with cooperation count ≥ 3.
        Order of rows does not matter.
    """
    result = (
        actor_director
            .groupby(['actor_id', 'director_id'], as_index=False)
            .size()                          # count rows per pair
            .query('size >= 3')              # keep pairs with ≥3 cooperations
            .loc[:, ['actor_id', 'director_id']]
    )

    return result
