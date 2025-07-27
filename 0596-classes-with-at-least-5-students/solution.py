import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    """
    Return a DataFrame of all classes that have at least five students.
    
    Parameters
    ----------
    courses : pd.DataFrame
        Input table with columns:
        - student : str  – student name (not needed for the final answer)
        - class   : str  – class name

    Returns
    -------
    pd.DataFrame
        Single‑column DataFrame with the column `class`, containing every
        class that has five or more distinct students.  Order does not matter.
    """
    # 1) Count how many rows (students) belong to each class
    #    After groupby, the result has two columns: `class` and `student` (the count).
    counts = (
        courses.groupby('class', as_index=False)['student']
               .count()
    )

    # 2) Keep only classes where the student count is >= 5
    qualifying = counts[counts['student'] >= 5]

    # 3) Return only the `class` column to match the required output schema
    return qualifying[['class']]

