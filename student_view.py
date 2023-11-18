"""
File Name:      student_view.py
Program Name:   Classroom Cold-Call Assist Software Program
Class:          CIS 422 - Winter22 - University of Oregon
Date Created:   1/14/2022
Authors:        Rebecca Hu
                Xiang Hao
                Ginni Gallagher
                Riana Valenzuela
Description: This file is the interface file, we can add 4 students at the beginning
    and then the user can use the leftKey, rightKey to move the highlight mouse, use the upKey to flag one student,
    use the downKey to remove one student from the interface and add one student automatically.

Note: Use the rightKey at the beginning.
"""

import tkinter as tk
import io_interface
import queue_manager
import student_data
import test_randomness

# set variables to store some information
# name_dic and email_dic help to store the students' names and emails, this helps to send data to student_data and queue_manager
name_dic = {}
email_dic = {}
performance = {}
# buttonL is a list to store the button, this list helps to highlight students' names
buttonL = []
# key_count helps to count the times of pressing keys, this helps to trach the key
key_count = -1
# b_row and b_col is the location where we put the button of student's name
b_row = 0
b_col = 50
# count is a gobal variable for funtion counter
count = 0
# key_add = 0
# call_times is the variable to count the times that the instructor
call_times = 0

# This function is the interface of students
def student_interface():
    global call_times
    call_times += 1
    # this if statement used to reset the variable if the instructor jump to student interface several times.
    if call_times > 1:
        global name_dic, email_dic, performance, buttonL, key_count, b_row, b_col, count
        # name_dic and email_dic help to store the students' names and emails, this helps to send data to student_data and queue_manager
        name_dic = {}
        email_dic = {}
        performance = {}
        # buttonL is a list to store the button, this list helps to highlight students' names
        buttonL = []
        # key_count helps to count the times of pressing keys, this helps to trach the key
        key_count = -1
        # b_row and b_col is the location where we put the button of student's name
        b_row = 0
        b_col = 50
        # count is a gobal variable for funtion counter
        count = 0
    # count = 0
    # This function help to count the times of adding students at the beginning of the system
    def counter():
        global count
        count = count + 1
        # print(count)

    # This function is called when the instructor want to add students to the deck at the beginning
    def roll_call():
        global b_row, b_col
        global b_1, b_2, b_3, b_4
        for i in range(4):
            get_name = queue_manager.queue_output_manager()
            # print("get name", get_name)
            name = get_name[0]
            # print(name)
            counter()
            b_row += 120
            if (count == 1):
                name_dic["0"] = name
                # use the number as the key instead of the name to prevent duplicate name
                email_dic["0"] = get_name[1]
                b_1 = tk.Button(call, text=name, activebackground="#ffffff", activeforeground="white")
                buttonL.append(b_1)
                b_1.place(x=b_row, y=b_col)
            elif count == 2:
                name_dic["1"] = name
                email_dic["1"] = get_name[1]
                b_2 = tk.Button(call, text=name, activebackground="#ffffff", activeforeground="white")
                buttonL.append(b_2)
                b_2.place(x=b_row, y=b_col)
            elif count == 3:
                name_dic["2"] = name
                email_dic["2"] = get_name[1]
                b_3 = tk.Button(call, text=name, activebackground="#ffffff", activeforeground="white")
                buttonL.append(b_3)
                b_3.place(x=b_row, y=b_col)
            elif count == 4:
                name_dic["3"] = name
                email_dic["3"] = get_name[1]
                b_4 = tk.Button(call, text=name, activebackground="#ffffff", activeforeground="white")
                buttonL.append(b_4)
                b_4.place(x=b_row, y=b_col)

            # print("initial", name_dic, email_dic, get_name)
        # print("c", b_row)
        # print(name_dic)
        # print("initial buttonL", buttonL)
        # print("row, col", b_row, b_col)


    # The function is called when the instructor press the leftkey, the red highlight will move to left
    def leftKey(event):
        global key_count
        # print("left0", key_count)
        if key_count == 0:
            buttonL[key_count].configure(highlightbackground='red')
        elif key_count > 0 and key_count < 4:
            buttonL[key_count].configure(highlightbackground='white')
            buttonL[key_count-1].configure(highlightbackground='red')
            key_count -= 1
            # if key_count == 0:
            #     key_count = 1
        # print("left1", key_count)
        # return

    # The function is called when the instructor press the rightKey, the red highlight will move to right
    def rightKey(event):
        global key_count
        try:
            # print("right0", key_count)
            if key_count < 4:
                key_count += 1
                if key_count == 0:
                    buttonL[key_count].configure(highlightbackground='red')
                    #     key_count += 1
                else:
                    buttonL[key_count - 1].configure(highlightbackground='white')
                    buttonL[key_count].configure(highlightbackground='red')
        except:
            print("You cannot press the right key if you are in the last student's name")
            key_count = 3
            buttonL[key_count].configure(highlightbackground='red')
            print(key_count)

    # The function is called when the instructor press upKey and this student will be flagged,
    # removed from the deck, and marked with bad
    def upKey(event):
        global key_count
        buttonL[key_count].destroy()
        buttonL.pop(key_count)
        if key_count == 0:
            # performance[name_dic['0']] = "bad"
            student_data.student_called(email_dic["0"], "bad")
            name_li = split_name(name_dic["0"])
            tuple_send = (name_li[0], name_li[1], email_dic["0"])
            queue_manager.queue_input_manager(tuple_send)
            email_dic.pop('0')
            name_dic.pop('0')
        elif key_count == 1:
            # performance[name_dic['1']] = "bad"
            student_data.student_called(email_dic["1"], "bad")
            name_li = split_name(name_dic["1"])
            tuple_send = (name_li[0], name_li[1], email_dic["1"])
            queue_manager.queue_input_manager(tuple_send)
            email_dic.pop('1')
            name_dic.pop('1')
        elif key_count == 2:
            # performance[name_dic['2']] = "bad"
            student_data.student_called(email_dic["2"], "bad")
            name_li = split_name(name_dic["2"])
            tuple_send = (name_li[0], name_li[1], email_dic["2"])
            queue_manager.queue_input_manager(tuple_send)
            email_dic.pop('2')
            name_dic.pop('2')
        elif key_count == 3:
            # performance[name_dic['3']] = "bad"
            student_data.student_called(email_dic["3"], "bad")
            name_li = split_name(name_dic["3"])
            tuple_send = (name_li[0], name_li[1], email_dic["3"])
            queue_manager.queue_input_manager(tuple_send)
            email_dic.pop('3')
            name_dic.pop('3')
        sort(event)
        # student_data.student_called(get_name[1], "bad")
        b_row = 600
        add_student(event)
        # print(buttonL)
        key_count = -1
        # print("performance up",performance)

    # The function is called when the instructor press downKey and this student will be removed and marked with good
    def downKey(event):
        global key_count
        print("destroy number", key_count)
        buttonL[key_count].destroy()
        buttonL.pop(key_count)
        if key_count == 0:
            # performance[name_dic['0']] = "good"
            student_data.student_called(email_dic["0"], "good")
            name_li = split_name(name_dic["0"])
            tuple_send = (name_li[0], name_li[1], email_dic["0"])
            queue_manager.queue_input_manager(tuple_send)
            email_dic.pop('0')
            name_dic.pop('0')
        elif key_count == 1:
            # performance[name_dic['1']] = "good"
            student_data.student_called(email_dic["1"], "good")
            name_li = split_name(name_dic["1"])
            tuple_send = (name_li[0], name_li[1], email_dic["1"])
            queue_manager.queue_input_manager(tuple_send)
            email_dic.pop('1')
            name_dic.pop('1')
        elif key_count == 2:
            # performance[name_dic['2']] = "good"
            student_data.student_called(email_dic["2"], "good")
            name_li = split_name(name_dic["2"])
            tuple_send = (name_li[0], name_li[1], email_dic["2"])
            queue_manager.queue_input_manager(tuple_send)
            email_dic.pop('2')
            name_dic.pop('2')
        elif key_count == 3:
            # performance[name_dic['3']] = "good"
            student_data.student_called(email_dic["3"], "good")
            name_li = split_name(name_dic["3"])
            tuple_send = (name_li[0], name_li[1], email_dic["3"])
            queue_manager.queue_input_manager(tuple_send)
            email_dic.pop('3')
            name_dic.pop('3')
        print(name_dic)
        sort(event)
        b_row = 600
        # print(b_row)
        add_student(event)
        print(buttonL)
        key_count = -1
        # print("performance up", performance)

    # This is a helper function to help to resort the students' names after remove one student from the deck
    def sort(event):
        # print(b_row)
        print("before sort", name_dic)
        global b_1, b_2, b_3, b_4
        if '0' not in name_dic.keys():
            b_1 = b_2
            b_2 = b_3
            b_3 = b_4
            b_3.place(x=(b_row - 150), y=b_col)
            b_2.place(x=(b_row - 300), y=b_col)
            b_1.place(x=(b_row - 450), y=b_col)
            name_dic["0"] = name_dic["1"]
            name_dic["1"] = name_dic["2"]
            name_dic["2"] = name_dic["3"]
            email_dic["0"] = email_dic["1"]
            email_dic["1"] = email_dic["2"]
            email_dic["2"] = email_dic["3"]
        elif '1' not in name_dic.keys():
            b_2 = b_3
            b_3 = b_4
            b_3.place(x=(b_row - 150), y=b_col)
            b_2.place(x=(b_row - 300), y=b_col)
            name_dic["1"] = name_dic["2"]
            name_dic["2"] = name_dic["3"]
            email_dic["1"] = email_dic["2"]
            email_dic["2"] = email_dic["3"]

        elif '2' not in name_dic.keys():
            b_3 = b_4
            b_3.place(x=(b_row - 150), y=b_col)
            name_dic["2"] = name_dic["3"]
            email_dic["2"] = email_dic["3"]
        # print("after sort", name_dic)

    # This is a helper function to help to add a student name to the interface after removing and sorting the students' names
    def add_student(event):
        global b_1, b_2, b_3, b_4
        get_name = queue_manager.queue_output_manager()
        # print("get name", get_name)
        name = get_name[0]

        name_dic["3"] = name
        email_dic["3"] = get_name[1]
        b_4 = tk.Button(call, text=name, activebackground="#ffffff", activeforeground="white")
        buttonL.append(b_4)
        b_4.place(x=b_row, y=b_col)
        # print("after adding auto", name_dic, email_dic, get_name)
        # print(buttonL)

    # This function is called when the intructor wants to return to the instructor's interface
    def to_instructor():
        call.destroy()
        io_interface.professor_view()

    # This function is a helper function to help to split the student's full name with a space
    def split_name(name):
        name_split = name.split(" ")
        return name_split

    # This the main part of the student interface, this part create the interface board by using tkinter
    call = tk.Tk()
    # set window size and title
    call.title('On-deck')
    call.geometry('700x100')

    # This function help to recognize the keyboard to call the corresponding functions
    def call_key(event):
        # global key_add
        # if event.char == "a":
        #     key_add += 1
        #     if key_add == 1:
        #         roll_call()
        if event.char == "s":
            export_data()
        elif event.char == "x":
            test_randomness.test_randomness()


    # This is a help function to call the export_data funtion in student_data file
    def export_data():
        student_data.export_data()

    b1 = tk.Button(call, bg='red', text="instructor view", width=12, height=2, font=('Helvetica', '10'), command=to_instructor)
    b1.place(x=10, y=10)

    roll_call()

    # Tkinter provide bind to track the key
    call.bind('<Left>', leftKey)
    call.bind('<Right>', rightKey)
    call.bind('<Up>', upKey)
    call.bind('<Down>', downKey)
    call.bind('<Key>', call_key)
    call.bind('<Escape>', quit)

    call.mainloop()
