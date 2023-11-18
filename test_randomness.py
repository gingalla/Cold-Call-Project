"""
File Name:      test_randomness.py
Program Name:   Classroom Cold-Call Assist Software Program 
Class:          CIS 422 - Winter22 - University of Oregon
Date Created:   1/16/2022
Authors:        Ginni Gallagher
                Rebecca Hu
                Xiang Hao
                Riana Valenzuela

This file consists of the logic for Random Distribution Verification.

Calling test_randomness() initiates 100 iterations of a system startup
simulation to test whether or not the organization of the student queue
is equitably random and does not favor certain student names over others. 

An output file titled 'Random_Distribution_Verification_output.txt' will
be place in user's cwd after test_randomness() is called. This file will
contain a summary report of the frequency of each student name.
"""
import random
from student_data import get_data
import os


"""
Driver function to test if the randomizer algorithms used in this system
maintain random results.

No Parameters or Returns
"""
def test_randomness():
    # File is used as intermediate storage for testing results
    # Will overwrite file if it already exists
    f = open('rdv_intermediate.txt', 'w')
    f.close

    # Iterate 100 times
    # Logic was created with system restart in mind 
    # - this functionality would be added in second version
    num_lines = 0
    while (num_lines < 99):
        num_lines = read_file_lines('rdv_intermediate.txt')

        f = open('rdv_intermediate.txt', 'a')

        # Retrieve data from pickle file
        student_information = get_data().values()

        # Separate student name from student information
        student_list = []
        for student in student_information:
            student_name = student[0] + " " + student[1]
            student_list.append(student_name)

        # Randomization of student names; simulates what happens upon system startup
        randomize_students(student_list)

        # Write first name from randomized queue to intermediate data file
        f.write(student_list[0])
        f.write('\n')

        f.close

    # After 100 iterations, format the output of collected data
    assemble_output(student_list)


"""
Helper function to randomize the student data. Separated into its own function in order
to allow future alterations to randomization method if desired.

Parameters
___________
student_list: list
    The list of student information
"""
def randomize_students(student_list):
    # Python built-in random module shuffle method
    random.shuffle(student_list)


"""
Helper function to read number of lines in intermediate file - translates to number of iterations.

Parameters
___________
file: str
    Name of file to be read


Return
______
num_lines: int
    Number of lines in the file
"""
def read_file_lines(file):
    f = open(file, 'r')

    # read number of lines in file
    lines = f.readlines()

    # count number of lines in file
    num_lines = 0
    for line in lines:
        num_lines += 1

    f.close

    return num_lines


"""
Function to format the output summary of results from randomize test.

Parameters
__________
student_list: list
    Intermediate list from test_randomness() of 100 randomly generated student names
"""
def assemble_output(student_list):
    output = open('Random_Distribution_Verification_output.txt', 'w')
    input_count = open('rdv_intermediate.txt', 'r')

    # Find frequency of each student name's occurance
    i = 0
    student_counts = []
    for student in input_count:
        student_counts.append(student.strip())

    # Alphabatize list for output file
    student_list.sort()

    # Count frequency of each name and write to file
    freq = 0
    for student in student_list:
        freq = student_counts.count(student)
        output.write("%s : %d \n" % (student, freq))

    input_count.close()
    output.close()

    # Clean directory by removing rdv_intermediate.txt
    os.remove('rdv_intermediate.txt')
