# This function should return a number (final grade). There are four types of final grades
# 100, if a grade for the exam is more than 90 or if a number of completed projects more than 10.
# 90, if a grade for the exam is more than 75 and if a number of completed projects is minimum 5.
# 75, if a grade for the exam is more than 50 and if a number of completed projects is minimum 2.
# 0, in other cases


def final_grade(exam, projects):
    if exam > 90 or projects > 10:    return 100
    elif exam > 75 and projects >= 5: return 90
    elif exam > 50 and projects >= 2: return 75
    else: return 0
        