from math import sqrt

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

print float(2 ** (1/2)) 

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / len(grades)
    return average

average = grades_average(grades)

def grades_variance(grades,average):
    total = 0
    for grade in grades:
        total += (grade - average) ** 2
    variance = float(total) / len(grades) 
    return variance

variance = grades_variance(grades, average)

def grades_std_deviation(variance):
    print variance
    std_deviation = sqrt(variance)
    return std_deviation
    
print grades_std_deviation(variance)