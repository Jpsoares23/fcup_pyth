def grade_table(grade: float) -> str:
    if grade < 0 or grade > 20:
        return 'Invalid'

    grading_table = {
        'Insufficient': (0, 4.9),
        'Not Sufficient': (5, 9.9),
        'Sufficient': (10, 11.9),
        'Good': (12, 14.9),
        'Very Good': (15, 18.9),
        'Excellent': (19, 20),
    }

    for category, (min_val, max_val) in grading_table.items():
        if min_val <= round(grade, 2) <= max_val:
            return category


print(grade_table(float(input('Write the grade [0, 20]: '))))
