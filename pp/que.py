#making file for database
db = open("studb.txt", "a")
def add():
	while True:
		rollno = int(input("Roll No: "))
		name = input("Name: ")
		marks = int(input("Marks:"))
		to_add = f"{str(rollno)},{name},{marks}}"
		db.write(to_add)
		break
		#if input("Continue: [leave empty if leave]") and :
			#db.write(to_add)
def search(rollno):
	db.close()
	db = open("studb.txt", "r")
	for x in db.readlines():
		if rollno == x[]
	
while True:
	print("1. Add Record")
	
	choice = int(input("Choice: "))
	if choice == 1:
		add()
