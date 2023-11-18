"""
File Name:      io_interface.py
Program Name:   Classroom Cold-Call Assist Software Program 
Class:          CIS 422 - Winter22 - University of Oregon
Date Created:   1/20/2022
Authors:        Ginni Gallagher
                Rebecca Hu
                Xiang Hao
                Riana Valenzuela

This file consists of logic to display the instructor view interface and allow imports and exports of tab-delimited 
text files containing student data.
"""
import tkinter as tk
import student_data
import student_view

"""
Function to display instructor view interface
"""
def professor_view():
    # Use TKinter to create window
    call = tk.Tk()
    call.title('Instructor View')
    call.resizable(False, False)
    call.geometry('350x700')

    # Function to switch to student view
    def to_student():
        call.destroy()
        student_view.student_interface()

    # Function that displays current students stored in system
    student_list = "Current students:\n\n"
    if student_data.get_data():
        current_students = student_data.get_data()
        for student, student_info in current_students.items():
            student_list += student_info[0]
            student_list += ' '
            student_list += student_info[1]
            student_list += '\n'

    # Current student text window
    students = tk.Label(call, text=student_list, justify='left').place(relx = 0.03,
                   rely = 0.02,
                   anchor = 'nw')

    # Import and export data buttons
    b1 = tk.Button(call, bg='red', text="Import data", width=10, height=2, command=student_data.input_data)
    b1.place(x=250, y=10)
    b2 = tk.Button(call, bg='red', text="Export data", width=10, height=2, command=student_data.export_data)
    b2.place(x=250, y=70)
    # Button to navigate to student view
    b3 = tk.Button(call, bg='red', text="Student view", width=10, height=2, command=to_student)
    b3.place(x=250, y=130)

    # the instructor can use escape key to quit the interface
    call.bind('<Escape>', quit)

    call.mainloop()
