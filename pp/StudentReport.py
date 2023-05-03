#1 moment 1 mode open, 1 file at a time, use a text file as database
# Student Report Card
# while loop input rollno, name, marks (for each subject)
# exit loop and add info to file when pressed ctrl + z
import os

file = 'studentdb.txt'
def terminalclear():
    if os.name == "nt": #windows system
        os.system("cls")
    else:
	    os.system("clear")

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
        os.system('clear')
        roll_num = input("Roll Number: ")
        if roll_num == "0":
            break
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
    terminalclear()
    with open(file) as db:
        print(db.read())

def remove():
    a = input("Roll Number To Delete: ")
    db = open(file, "r")
    temp = open('temp.tmp', "w")
    tempvar = []
    for x in db.readlines():
        if x[0] != a:
            tempvar.append(x)

    db.close()
    os.remove(file)
    for somethingthingthingy in tempvar:
        temp.write(somethingthingthingy)
    temp.close()
    os.rename('temp.tmp', file)


def clear():
    db = open(file, "w")
    db.write("")
    db.close()

def menu():
    terminalclear()
    while True:
        print("1. Add Report")
        print("2. View Records")
        print("3: Clear Records💀")
        print("4: Delete Records")
        choice = int(input("Choice: "))
        if choice == 1:
            add()
        elif choice == 2:
            read()
        elif choice == 3:
            clear()
        elif choice == 4:
            remove()
            
from pathlib import Path
if Path('studentdb.txt').is_file():
    menu()
else:
    print("No Database Found!")
    quit()
