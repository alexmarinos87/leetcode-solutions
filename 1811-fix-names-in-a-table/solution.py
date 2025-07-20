import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    # .str.capitalize(): first char -> upper, rest -> lower
    users["name"] = users["name"].str.capitalize()
    
    # Return required columns, ordered by user_id
    return users[["user_id", "name"]].sort_values("user_id").reset_index(drop=True)

