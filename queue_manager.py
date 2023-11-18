"""
File Name:      queue_manager.py
Program Name:   Classroom Cold-Call Assist Software Program 
Class:          CIS 422 - Winter22 - University of Oregon
Date Created:   1/18/2022
Authors:        Ginni Gallagher
                Rebecca Hu
                Xiang Hao
                Riana Valenzuela

This file consists of the primary functionality of queue management. The queue is the data structure containing 
every student on the student roster at all times. The queue is randomly populated and randomized after each
full iteration through the student roster. This file manages sending and receiving queue information
"""
from queue import Queue
import random
import student_data

# Global variable set to true to indicate system startup
starting_system = True

# Tracks the first entry in the queue
first_entry = []

# Global queue - can be accessed by all functions in this file
global student_queue
student_queue = Queue()


"""
Function to manage setting up the randomly organized queue at the start of the systems lifespan.
Function also sends names from the queue to the user interface.

Return
_______
send_student_data: tuple
    Tuple consisting of student first and last name and their uoemail (key into pickle dict)
"""
def queue_output_manager():
    global starting_system

    # If this is system startup, load the global queue
    if (starting_system == True):
        # Retrieve student data from pickle file
        student_dict = student_data.get_data()

        # Randomize order of students
        dict_values = list(student_dict.values())
        random.shuffle(dict_values)

        # Add relevant student information queue
        queue_names = []
        for student in dict_values:
            student_info = (student[0], student[1], student[3])
            queue_names.append(student_info)

        # Keep track of first name on the queue 
        global first_entry
        first_entry = queue_names[0][0] + queue_names[0][1]

        # Populate the student queue with student values from dict
        for student in queue_names:
            student_queue.put(student)

    # After initial start-up, global will be set to false; queue will already be set
    starting_system = False

    # Holds dict values for student in front of the queue
    first_student_info = student_queue.get()

    # Concatenate student first and last name to one string
    student_first_name = first_student_info[0]
    student_last_name = first_student_info[1]
    student_name = student_first_name + " " + student_last_name

    # First_student_info[2] is the key to access the dict
    send_student_data = (student_name, first_student_info[2])

    return send_student_data


"""
Function to manage re-inserting names into the queue after they have been removed
from on-deck list. Function also checks that the returned name is not the same name 
as the first name initially on the list. If it is, the system calls to reshuffle the
queue order to maintain optimal randomness.

Parameter
_________
received_student_data: tuple
    Tuple containing student name and uoemail
"""
def queue_input_manager(received_student_data):

    # Concatenate the first and last name to check against first entry name
    student_received = received_student_data[0] + received_student_data[1]
    if (student_received == first_entry):
        reshuffle_queue()

    # Add name back to the queue
    student_queue.put(received_student_data)
    return


"""
Helper function to reshuffle the queue.
"""
def reshuffle_queue():
    student_dict = []

    # Remove all students from queue
    while (student_queue.empty() != True):
        student_dict.append(student_queue.get())

    # Randomize order of students
    random.shuffle(student_dict)

    # Re-populate the student queue with student values from dict
    for student in student_dict:
        student_queue.put(student)
        print(student)

    return
