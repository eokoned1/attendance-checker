"""
File: p1.py
Author: Mofe Okonedo
Date: 09/06/23
Email:  eokoned1@umbc.edu
Description:  This program scans through a list of class rosters and keeps track of attendance
"""


debug = False

from dataEntry import fill_roster
from dataEntry import fill_attendance_data



def list_students_not_in_class(class_roster, attend_data):
    no_show = []
    for student in class_roster:
        current_student = False
    for students in attend_data:
        if class_roster[i] in students:
            current_student = True

    if not current_student:
        no_show.append(class_roster[i])

    return no_show


"""
Compare the swipe log with the given course roster. Place those students that
did not show up for class into a list.
:param ????: 
:param ????:
:return: ????
"""


def list_all_times_checking_in_and_out(name_student, attend_data):
    students_check_in_out = []
    for student in attend_data:
        if name_student in student:
            students_check_in_out.append(student)

    return students_check_in_out


"""
Looking at the swiping log, this function will list all in and outs for a
particular Student. Please note, as coded in the p1.py file given, this
function was called three times with different student values. 
:param ????: 
:param ????:
:return: ????
"""


def list_all_times_checked_in(name_student, attend_data):
    name_student = ''.join(name_student[2])
    the_time = name_student.split(':')
    print(type(the_time))
    """
    This function returns a list of when all student(s) FIRST swipe in.
    :param ????:
    :param ????:
    :return: ????
    """


def list_students_late_to_class(time, attend_data):
    """
    When given a timestamp string and the swipe log, a list of those records
    of students who swiped in late into the class is produced. This function
    returns a list of when all student(s) FIRST swipe in.
    :param ????:
    :param ????:
    :return: ????
    """


def get_first_student_to_enter(attend_data):
    """
    Simply, this function returns the student that swiped in first. Note,
    the order of the data entered into the swipe log as not the earliest
    student to enter.
    :param ????:
    :param ????:
    :return: ????
    """

    j = []
    k = []
    counter = 0
    new_list = []

    for i in range(len(attend_data)):
        new_list.append(attend_data[i].split(","))

    for i in range(len(new_list)):
        counter = 0
        for l in range(len(new_list)):

            if new_list[i][2] < new_list[l][2]:
                counter += 1
            if counter == len(new_list) - 1:
                j.append(new_list[i])
                f = ', '.join(new_list[i])
                k.append(f)
                return k[0]





def printList(the_list):
    """
    Simply prints the list. The function should not be able to change any
    values of that list passed in.
    :param ????:
    :param ????:
    :return: ????
    """


''' ***** LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE *************** '''

if __name__ == '__main__':
    # Example, Dr. NIcholas, 9am class

    # load class roster here into a list
    classRoster = fill_roster()

    # figure out which attendance data file to load here

    # load data
    attendData = fill_attendance_data()

    # use different tests
    # make sure roster was filled
    # printList(classRoster)
    # make sure attendance data was loaded
    # printList(attendData)

    # list all those missing
    print("****** Students missing in class *************")
    printList(list_students_not_in_class(classRoster, attendData))
    # list signin/out times for a student
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Lupoli, Shawn", attendData))
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Allgood, Nick", attendData))
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Arsenault, Al", attendData))
    # display when students first signed in (and in attendance)
    print("****** Check in times for all students who attended***")
    printList(list_all_times_checked_in(attendData))
    # display all of those students late to class
    print("****** Students that arrived late ********************")
    printList(list_students_late_to_class("09:00:00", attendData))
    # display first student to enter class
    print("******* Get 1st student to enter class ****************")
    print(get_first_student_to_enter(attendData))


