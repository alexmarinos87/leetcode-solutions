import pandas as pd

def students_and_examinations(students: pd.DataFrame,
                              subjects: pd.DataFrame,
                              examinations: pd.DataFrame) -> pd.DataFrame:
    """
    For every student–subject pair, count how many times that student took
    that subject’s exam.

    Parameters
    ----------
    students : pd.DataFrame
        Columns: student_id, student_name
    subjects : pd.DataFrame
        Columns: subject_name
    examinations : pd.DataFrame
        Columns: student_id, subject_name (may contain duplicates)

    Returns
    -------
    pd.DataFrame
        Columns (ordered): student_id, student_name, subject_name, attended_exams
        Sorted by student_id then subject_name.
    """

    # ───────────────────────────────────────────────────────
    # 1)  Pre‑aggregate: count exam rows per (student, subject)
    # ───────────────────────────────────────────────────────
    exam_counts = (
        examinations.groupby(['student_id', 'subject_name'])
                    .size()                                   # number of rows
                    .reset_index(name='attended_exams')       # keep as a column
    )

    # ───────────────────────────────────────────────────────
    # 2)  Cartesian product of all students × all subjects
    #     (every student takes every course)
    # ───────────────────────────────────────────────────────
    cross = (
        students.assign(key=1)
                .merge(subjects.assign(key=1), on='key')
                .drop(columns='key')                         # remove helper col
    )

    # ───────────────────────────────────────────────────────
    # 3)  Attach the counts; missing combos → 0
    # ───────────────────────────────────────────────────────
    result = (
        cross.merge(exam_counts, on=['student_id', 'subject_name'], how='left')
             .fillna({'attended_exams': 0})                 # NaN → 0
             .astype({'attended_exams': int})               # ensure int dtype
             .sort_values(['student_id', 'subject_name'])   # required ordering
             .reset_index(drop=True)
    )

    # Keep columns in the order the problem expects
    return result[['student_id', 'student_name', 'subject_name', 'attended_exams']]

