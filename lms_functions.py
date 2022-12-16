#lms.py
#This program is a simple Library Management System that handles
#borrowing, returning and inventory. Additionally, one is able to
#know who has what books.


library_books = {"Learn Python": 5, "Pandas": 8,
                     "Machine Learning": 2, "Statistics": 3, "Begin to Code": 4}


def menu():

        print('''..........JENGA Library Management System...............

               Select Options
               1: add a book
               2: borrow a book
               3: return a book
               4: view books
               0: Exit
                ''')
        

def add_books():
    num = int(input("How many books would you like to add?: "))
    for item in range(1,num + 1):
        item = input("Enter book title: ")
        count = int(input("Enter the total number of books: "))
        library_books[item] = count
       

def borrow_books():
    students = {}
    book_issued = {}
    item = input("Enter the book title you'd like to borrow: ")
    if item in library_books:
        student_name = input("Enter your student name: ")
        student_id = input("Enter student id: ")
        library_books[item]= (library_books[item]) - 1
        students[student_id] = student_name
        book_issued[student_name] = item
        print(students[student_id],"has",book_issued[students[student_id]],"Book.")

    else:
        print("Book unvailable")

def return_books():
    item = input("Enter the book title you are returning: ")
    if item in library_books:
        library_books[item]+= 1
        print(f"{item} book returned successfully.")
    else:
        print(f"Sorry, {item} is not a library book.")
def view_books():  
    print(f'{"BOOKS":<18}COUNT')
    for item, count in sorted(library_books.items()):
        print(f"{item:<20}{count}")


def main():
    menu()
    option = int(input("Enter an option: "))
    while option != 0:
        if option == 1:
            add_books()
            
        elif option == 2:
            borrow_books()
            
        elif option == 3:
            return_books()

        elif option == 4:
            view_books()
        else:
                print("Sorry, invalid option")

        option = int(input("\nEnter an option: "))
        
        
    print("*** Thank you for using this program, Goodbye ***")
    print('_' * 55)
           
main()   
    

