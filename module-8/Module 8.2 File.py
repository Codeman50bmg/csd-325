#Steven Skinner
#Module 8.2

import json

# Step 1: Load the JSON file into a Python list
def load_students(filename):
    with open(filename, 'r') as file:
        students = json.load(file)  # Load the JSON data into a Python list of dictionaries
    return students

# Step 2: Function to print each student in the specified format
def print_student_list(students):
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# Step 3: Add a new student to the list
def add_student(students, last_name, first_name, student_id, email):
    new_student = {
        "F_Name": first_name,
        "L_Name": last_name,
        "Student_ID": student_id,
        "Email": email
    }
    students.append(new_student)  # Add new student to the list

# Step 4: Save the updated student list to the JSON file
def save_students(filename, students):
    with open(filename, 'w') as file:
        json.dump(students, file, indent=4)  # Save the list back to the JSON file with indentation

# Main function to execute the tasks
def main():
    filename = r'c:\School\Advanced python\Module 8\student.json'  # Correct file path
    
    # Load the students data from the JSON file
    students = load_students(filename)

    # Notify the user that this is the original student list
    print("Original Student List:")
    
    # Print out the student list
    print_student_list(students)

    # Add a new student to the list
    new_last_name = "Steven"
    new_first_name = "Skinner"
    new_student_id = "191145"
    new_email = "StevenSkinner@example.com"
    
    # Notify user about the update
    print("\nAdding a new student to the list...")

    add_student(students, new_last_name, new_first_name, new_student_id, new_email)

    # Notify the user that this is the updated student list
    print("\nUpdated Student List:")
    
    # Print out the updated student list
    print_student_list(students)

    # Save the updated list back to the JSON file
    save_students(filename, students)

    # Notify the user that the file has been updated
    print("\nThe student list has been updated in the JSON file.")

if __name__ == "__main__":
    main()
