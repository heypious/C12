#1 moment 1 mode open, 1 file at a time, use a text file as database
# Student Report Card
# while loop input rollno, name, marks (for each subject)
# exit loop and add info to file when pressed ctrl + z
from os import system as terminal
from prettytable import from_csv as csv

file = 'studentdb.csv'

def write(data):
    db = open(file, "a")
    db.write(data)
    db.close()

def roll_is_there(data):
    db = open(file, "r")
    for x in db.readlines():
        record = x.split(",")
        if record[0] == data:
            return True
        else:
            return False
    db.close()

def add():
    print('Add Report Page')
    while True:
        terminal('cls')
        roll_num = input("Roll Number: ")
        name = input("Name: ")
        marks = input("Marks: ")
        data = f"{roll_num},{name},{marks}\n"
        if roll_is_there(roll_num):
            print(f"Roll Number {roll_num} already exists.")
            quit()
        else:
            write(data)
            print(f"{data} added to {file}")

def read():
    terminal('cls')
    with open(file, "r") as db:
        mytable = csv(db)
        print(mytable)

def clear():
    db = open(file, "w")
    db.write("")
    db.close()

def menu():
    terminal('cls')
    while True:
        print("1. Add Report")
        print("2. View Records")
        print("3: Clear Records💀")
        choice = int(input("Choice: "))
        if choice == 1:
            add()
        elif choice == 2:
            read()
        elif choice == 3:
            clear()
        else:
            quit()
            
from pathlib import Path
if Path('studentdb.csv').is_file():
    menu()
    
