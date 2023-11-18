"""
File Name:      student_data.py
Program Name:   Classroom Cold-Call Assist Software Program 
Class:          CIS 422 - Winter22 - University of Oregon
Date Created:   1/15/2022
Authors:        Ginni Gallagher
                Rebecca Hu
                Xiang Hao
                Riana Valenzuela

This file consists of student data management and input and export file logic.
"""

import os
from tkinter import filedialog, messagebox
import pickle
from datetime import date

# Global student data dictionary
student_data = {}

"""
Function to allow user to import data
This function is called when "input data" button is clicked
"""
def input_data():
    # Allows user to input text file
    file = filedialog.askopenfilename(
        title="Select a tab-delimited file with student data",
        filetypes=[('textfiles', '*.txt')])
    
    # If cancel button
    if not file: 
        return

    # Warning message for importing new data
    warning_message = "Do you want to import "
    warning_message += str(file)
    warning_message += "?"

    # Check if student data exists
    if get_data():
        warning_message = "The following student data will be overridden. Do you want to continue?\n\n"
        current_students = get_data()
        # List all current students being saved by system
        for student, student_info in current_students.items():
            warning_message += student_info[0]
            warning_message += ' '
            warning_message += student_info[1]
            warning_message += '\n'

    # Override warning
    confirm_override = messagebox.askyesno(
        title="Warning", 
        message=warning_message,
        default=messagebox.YES)

    # Cancel file input
    if not confirm_override:
        return

    # Reading file
    else:
        student_file = open(file, "r")
        # File headers
        headers = student_file.readline().strip().split('\t')

        # Populate dictionary with email as key
        for student in student_file:
            student = student.strip().split('\t')
            student[4] = []
            # Convert string number of flags to int
            student[5] = int(student[5])
            student[6] = int(student[6])
            student_data[student[3]] = student

    student_file.close()

    save_data(student_data)

"""
Function to save flag data when a student is flagged.
This function is called from student_view.py.

Parameters
_________
email: string
    String of unique student email
flag_type: string
    String of type of flag that was raised
    "good" or "bad"
"""
def student_called(email, flag_type):
    # Get student dictionary
    students = get_data()
    print(students)

    # Find student data through email as key
    student = students[email]

    # Increment type of flag
    if flag_type == 'good':
        student[5] += 1
    elif flag_type == 'bad':
        student[6] += 1
    else:
        print("Flag type must be 'good' or 'bad'")
        return
    
    # Track dates that student was called in format MM/DD/YYY
    student[4].append(date.today().strftime("%m/%d/%Y"))

    print("student called", student)

    # Save new data
    save_data(students)

"""
Function to extract student dictionary from pickle file
"""
def get_data():
    # If there is no student data
    if os.path.getsize('student_data.pickle') == 0:
        return False
    else:
        # Code from:
        # https://stackoverflow.com/questions/11218477/how-can-i-use-pickle-to-save-a-dict
        # Read from pickle file
        with open('student_data.pickle', 'rb') as handle:
            data = pickle.load(handle)
        return data

"""
Function to save student dictionary to pickle file

Parameters
__________
student_data: dict
    Dictionary containing student data
"""
def save_data(student_data):
    # Code from
    # https://stackoverflow.com/questions/11218477/how-can-i-use-pickle-to-save-a-dict
    # Save to pickle file
    with open('student_data.pickle', 'wb') as handle:
        pickle.dump(student_data, handle, protocol=pickle.HIGHEST_PROTOCOL)

"""
Function to generate a file about the information of the students to instructor
"""
def export_data():
    # containing total times called, number of flags, full name, 9-digit UO ID,
    # list of dates when student was called YY/MM/DD in order
    f = open("Student_information.txt", 'w+')
    title = "First Name	Last Name	UO ID	Email	(# of Good Flags)	(# of Bad Flags)  (# of total times called)    (Date(s) called) \n"
    f.write(title)
    with open('student_data.pickle', 'rb') as handle:
        data = pickle.load(handle)
        time = ""
        print(data)
        for each in data:
            # print("each", each)
            # print("called times", data[each][5], data[each][6])
            total = int(data[each][5]) + int(data[each][6])
            for info in data[each]:
                print("info",info)
                string = ''
                if isinstance(info, list):
                    time = str(info)
                else:
                    string += str(info)
                    string += "\t"
                f.write(string)
            f.write(str(total))
            f.write('\t')
            f.write(time)
            f.write('\n')
    f.close()

def main():
    print(student_data)

if __name__ == "__main__":
    main()