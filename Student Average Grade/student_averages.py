import csv
from collections import defaultdict

def calculate_averages(csv_file, output_file):
   
    student_grades = defaultdict(list)
    
    # Read the CSV file
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        
       
        for row in reader:
            student = row['Student']
            grade = float(row['Grade'])
            student_grades[student].append(grade)
    
    # Calculate average grades
    averages = {student: sum(grades) / len(grades) for student, grades in student_grades.items()}
    
    # Write the results to a new CSV file
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Student', 'Average Grade'])
        
        for student, average in averages.items():
            writer.writerow([student, average])
    
    print(f"Average grades have been saved to student_averages.csv")



input_file = 'Student Average Grade/student_grade.csv'  
output_file = 'Student Average Grade/student_averages.csv'  
    
calculate_averages(input_file, output_file)

