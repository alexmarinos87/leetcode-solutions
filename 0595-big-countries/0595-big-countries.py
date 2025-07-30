import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    """
    Return the name, population, and area of every country that is
    considered 'big':
        • area ≥ 3 000 000  OR
        • population ≥ 25 000 000

    Parameters
    ----------
    world : pd.DataFrame
        Columns: name, continent, area, population, gdp

    Returns
    -------
    pd.DataFrame
        Columns: name, population, area  (order does not matter).
    """
    mask = (world['area'] >= 3_000_000) | (world['population'] >= 25_000_000)
    return world.loc[mask, ['name', 'population', 'area']]
