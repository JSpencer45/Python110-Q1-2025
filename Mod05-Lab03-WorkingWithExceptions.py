# ------------------------------------------------------------------------------------------ #
# Title: Working With Dictionaries And Files
# Desc: Shows how work with dictionaries and files when using a table of data
# Change Log: (Who, When, What)
#   JSpencer,5/21/2025,Edited Script
# ------------------------------------------------------------------------------------------ #

import json  #import code from Python's JSON module into my script

# Define the Data Constants
FILE_NAME: str = 'MyLabData.json'

# Define the program's data
MENU: str = '''
----Student GPAs--------------------------------
    Select from the follwoing menu:
        1. Show current student data.
        2. Enter new student data.
        3. Save data to a file.
        4. Exit the program.
------------------------------------------------
'''

student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
student_gpa: float = 0.0  # Holds the GPA of a student entered by the user.
message: str = ''  # Holds a custom message string
menu_choice: str = ''   # Hold the choice made by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
file_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Not using type hint helps PyCharm, so we won't use it going forward


# When the program starts, read the file data into a list of dictionary rows (table)
# Extract the data from the file
#file = open(FILE_NAME, 'r')
#for row in file.readlines():
#    # Transform the data from the file
#    student_data = row.split(',')
#    student_data = {'FirstName': student_data[0],
#                    'LastName': student_data[1],
#                    'GPA': float(student_data[2].strip())}
#    # Load it into the collection (list of lists)
#    students.append(student_data)
# file.close

try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()

except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False:
        file.close()


while True:

    print(MENU)
    menu_choice = input("Enter your menu choice number: ")
    print()  # Adding extra space to make it look nicer.

    if menu_choice == "1":
    # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            if student["GPA"] >= 4.0:
                message = " {} {} earned an A with a {:.2f} GPA"
            elif student["GPA"] >= 3.0:
                message = " {} {} earned a B with a {:.2f} GPA"
            elif student["GPA"] >= 2.0:
                message = " {} {} earned a C with a {:.2f} GPA"
            elif student["GPA"] >= 1.0:
                message = " {} {} earned a D with a {:.2f} GPA"
            else:
                message = " {} {}'s {:.2f} GPA was not a passing grade"
            print(message.format(student["FirstName"], student["LastName"], student["GPA"]))
        print("-"*50)
    elif menu_choice == "2":
        try:
            # Input the data
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                    raise ValueError('The first name should not contain numbers!')
            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError('The last name should not contain numbers!')
            try:
                student_gpa = float(input("What is the student's GPA? "))
            except ValueError:
                raise ValueError('GPA must be a numeric value!')

            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "GPA": student_gpa}
            students.append(student_data)
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
    elif menu_choice == "3":
#        #  Save the data to the file
#        file = open(FILE_NAME, "w")
#        for student in students:
#            file.write(f'{student["FirstName"]},{student["LastName"]},{student["GPA"]}\n')
#        file.close()
#        print("Data Saved!")
#        continue
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent=2)
            file.close()
            continue
        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file.closed == False:
                file.close()

# Repeat the follow tasks
    # display the table's current data
   # Add data to the table
    # Save the data to the file
    # Exit the program


# Output the data

print(f"Student {student_first_name } {student_last_name} \
has a {student_gpa:.2f} grade point average (GPA)")
