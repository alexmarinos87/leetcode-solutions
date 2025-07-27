import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    result = (
        teacher.groupby('teacher_id', as_index=False)['subject_id']
               .nunique()                       # number of unique subjects
               .rename(columns={'subject_id': 'cnt'})
    )
    return result

