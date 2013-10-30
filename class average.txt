lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(x):
    y = sum(x)
    return float(y) / len(x)
    
def get_average(student):
    a = average(student["homework"])
    b = average(student["quizzes"])
    c = average(student["tests"])
    return a * 0.1 + b * 0.3 + c * 0.6
    
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 60 and score < 70:
        return "D"
    else:
        return "F"
        
students = [lloyd, alice, tyler]
L = get_average(lloyd)
print get_letter_grade(L)
            
def get_class_average(class_list):
    print len(class_list)
    class_average = 0.0
    for student in class_list:
        class_average += get_average(student)
    return class_average / len(class_list)
    
print get_class_average(students)
