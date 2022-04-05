from flask import Flask, request, render_template
import sqlite3
from sqlite3 import Error
import Tools.Books as BK
import Tools.Customers as CR

con = sqlite3.connect('Library.db', check_same_thread=False)

api = Flask(__name__)
cur = con.cursor()

def initDB():
    try:
        cur.execute('''CREATE TABLE Books
               (BookID int, Name text, Author text, Year int, Type int)''')
        cur.execute('''CREATE TABLE Customers
               (CustomerId int, Name text, City text, age int)''')
        cur.execute('''CREATE TABLE Loans
               (CustomerID int, BookID int, LoanDate int, ReturnDate int)''')

    except:
        print("Table already exist")
  
    con.commit()
initDB()

def addData():
    cur.execute('''INSERT INTO Books VALUES(11,"The Da Vinci Code", "Dan Brown", 2003, 1)''')
    cur.execute('''INSERT INTO Books VALUES(12,"Angels & Demons", "Dan Brown", 2000, 1)''')
    cur.execute('''INSERT INTO Books VALUES(13,"The Lost Symbol", "Dan Brown", 2009, 2)''')
    cur.execute('''INSERT INTO Books VALUES(14,"Origin", "Dan Brown", 2017, 1)''')
    cur.execute('''INSERT INTO Books VALUES(15,"The Secret", "Rhonda Byrne", 2006, 3)''')
    cur.execute('''INSERT INTO Books VALUES(16,"Harry Potter and the Chamber of Secrets", "J.K Rowling", 1998, 2)''')
    cur.execute('''INSERT INTO Books VALUES(17,"Harry Potter and the Prisoner of Azkaban", "J.K Rowling", 1999, 1)''')
    cur.execute('''INSERT INTO Customers VALUES(1,"Liron Nissim", "Tel Aviv", 32 )''')
    cur.execute('''INSERT INTO Customers VALUES(2,"Omer Gal", "Tel Aviv", 38 )''')
    cur.execute('''INSERT INTO Customers VALUES(3,"Shay Nir", "Haifa", 36 )''')
    cur.execute('''INSERT INTO Customers VALUES(4,"Noam Mosser", "Gan Yavne", 36 )''')
    cur.execute('''INSERT INTO Customers VALUES(5,"Neta Harel", "Tel Aviv", 22 )''')
    cur.execute('''INSERT INTO Customers VALUES(6,"Noa Agam", "Ashdod", 46 )''')
    con.commit()
addData()


@api.route("/", methods=['GET', 'POST'])
def homepage():
    return render_template("mainHomepage.html")


@api.route("/Books/bookHomepage", methods=['GET', 'POST'])
def books():
    return BK.Book.books(BK)


@api.route("/Books/addBook", methods=['GET', 'POST'])
def addBook():
    return BK.Book.addBook(BK)

@api.route("/Books/findBooksByName", methods=['GET','POST'])
def findBook():
    return BK.Book.findBook(BK.Book)


@api.route("/Books/bookHomepage", methods=['GET', 'POST'])
def removeBook():
    return BK.Book.removeBook(BK.Book)


# @api.route("/Books/removeBook", methods=['GET', 'POST'])
# def updateBook():
#     return BK.Book.updateBook(BK.Book)

@api.route("/Customers/CustHomepage", methods=['GET', 'POST'])
def CustHomepage():
    return render_template("/Customers/CustHomepage.html")


@api.route("/Customers/addCustomers", methods=['GET', 'POST'])
def addCustomer():
    return CR.Customers.addCustomers(CR.Customers)


# @api.route("/Customers/allCustomers", methods=['GET', 'POST'])
# def removeCustomers():
#     return CR.Customers.removeCustomers(CR.Customers)


@api.route("/Customers/allCustomers", methods=['GET', 'POST'])
def myCustomer():
    return CR.Customers.myCustomer(CR.Customers)

@api.route("/Customers/findCustomersByName", methods=['GET', 'POST'])
def findCustomers():
    return CR.Customers.findCustomers(CR.Customers)

if __name__ == '__main__':
    api.run(debug=True,port=9000)