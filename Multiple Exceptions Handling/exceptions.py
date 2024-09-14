import csv
import logging
from collections import defaultdict


logging.basicConfig(filename='error_log.txt', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_averages(csv_file, output_file):
    student_grades = defaultdict(list)
    
    try:
       
        with open(csv_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            
          
            if 'Student' not in reader.fieldnames or 'Grade' not in reader.fieldnames:
                raise KeyError("CSV file must contain 'Student' and 'Grade' columns")
            
            # Process each row
            for row in reader:
                try:
                    student = row['Student'].strip()
                    grade = float(row['Grade'].strip())
                    student_grades[student].append(grade)
                except ValueError as e:
                    logging.error(f"Value error in row {row}: {e}")
                    continue
                except KeyError as e:
                    logging.error(f"Missing expected column in row {row}: {e}")
                    continue

       
        averages = {student: sum(grades) / len(grades) for student, grades in student_grades.items()}

      
        with open(output_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Student', 'Average Grade'])
            
            for student, average in averages.items():
                writer.writerow([student, average])
        
        print(f"Average grades have been saved to student_average.csv'")

    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        print("Error: The file was not found.")
    except KeyError as e:
        logging.error(f"Missing expected columns in the file: {e}")
        print("Error: The CSV file does not contain the required columns.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print("An unexpected error occurred. Please check the error_log.txt file for details.")


input_file = 'Multiple Exceptions Handling/student_grades.csv'  
output_file = 'Multiple Exceptions Handling/student_average.csv'  
    
calculate_averages(input_file, output_file)


