#!/usr/bin/env python3

'''
OPS445 Assignment 1 - Winter 2023
Program: assignment1.py 
Author: "Student Name"
The python code in this file is original work written by
"Student Name". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: <Enter your documentation here>

Date: 
'''

def usage():
    "TODO enter docstring"
    pass # TODO: delete this line, replace with valid code.

def valid_date(date: str) -> bool:
    "TODO enter docstring"
    # return True or False 
    pass # TODO: delete this line, replace with valid code.

def leap_year(year: int) -> bool:
    "takes a year in YYYY format, and returns True if it's a leap year, False otherwise."
    # TODO reorganize code, enter code from after() here.
    pass # TODO: delete this line, replace with return statement.


def after(date: str) -> str: 
    "after takes a valid date string in YYYY format and returns"
    "a date string for the next day in YYYY-MM-DD format."
    if len(date) != 10:
        return '0000-00-00'
    else:
        str_year, str_month, str_day = date.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)

        lyear = year % 4 # TODO: put this into the function leap_year.
        if lyear == 0:
            feb_max = 29 
        else:
            feb_max = 28 

        lyear = year % 100
        if lyear == 0:
            feb_max = 28 

        lyear = year % 400
        if lyear == 0:
            feb_max = 29 

        tmp_day = day + 1 

        mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        if tmp_day > mon_max[month]:
            to_day = tmp_day % mon_max[month] # if tmp_day > this month's max, reset to 1
            tmp_month = month + 1
        else:
            to_day = tmp_day
            tmp_month = month + 0

        if tmp_month > 12:
            to_month = 1
            year = year + 1
        else:
            to_month = tmp_month + 0

        next_date = f"{year}-{to_month:02}-{to_day:02}"
        return next_date

def before(date: str) -> str:
    "TODO enter docstring."
    pass # TODO replace this with code, using your algorithm document.

def dbda(start_date: str, step: int) -> str:
    "given a start date and a number of days into the past/future, give date"
    # create a loop
    # call before() or after() as appropriate
    # return the date as a string YYYY-MM-DD
    pass

if __name__ == "__main__":
    # process command line arguments
    # call dbda()
    # output the result
    pass
