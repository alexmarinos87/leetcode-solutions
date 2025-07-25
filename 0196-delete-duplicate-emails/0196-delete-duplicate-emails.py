import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # 1️⃣  Make sure the lowest id for each email appears first
    person.sort_values('id', inplace=True)

    # 2️⃣  Drop all rows that have a duplicate email, except the first (lowest‑id) one
    person.drop_duplicates(subset='email', keep='first', inplace=True)

    # No return needed — the DataFrame is modified in place
