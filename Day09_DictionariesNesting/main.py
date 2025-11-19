# Day 9 - Student Grading Program

student_scores = {
    "Sommer": 92,
    "Alex": 85,
    "Jordan": 74,
    "Taylor": 59,
    "Mia": 100
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]

    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)