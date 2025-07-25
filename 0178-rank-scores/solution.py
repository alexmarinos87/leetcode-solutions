import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Dense‑rank the scores: highest score → rank 1, ties share the same rank
    scores['rank'] = scores['score'].rank(method='dense', ascending=False).astype(int)
    
    # Return the required columns, ordered by score descending
    return scores[['score', 'rank']].sort_values(by='score', ascending=False)

