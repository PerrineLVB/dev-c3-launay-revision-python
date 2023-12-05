student_grades = {
    'Antoine Dupont': 19,
    'Romain Ntamack': 18,
    'Thomas Ramos': 17,
    'François Cros': 15,
    'Julien Marchand': 16,
    'Melvyn Jaminet': 8,
    'Théo Ntamack': 13
}

student_grades_ordered = dict(sorted(student_grades.items(), key=lambda item: item[1], reverse=True))
#print(student_grades_ordered)

print(list(student_grades_ordered.keys())[0])