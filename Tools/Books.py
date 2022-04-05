from flask import render_template, request
import sqlite3

con=sqlite3.connect("Library.db", check_same_thread=False)
cur=con.cursor()

class Book:
    def __init__(self):
        pass

    def books(self):
        SQL=(f'''SELECT rowid, Name, Author, Year, Type FROM Books''')
        print(SQL)
        res= []
        for i in cur.execute (SQL):
            res.append({"id": i[0], "Name": i[1], "Author": i[2], "Year": i[3], "Type": i[4]})
        return render_template("/Books/bookHomepage.html", books=res)

    def addBook(self):
        msg=""
        if request.method=='POST':
            bName = request.form.get('Name')
            bAuthor = request.form.get('Author')
            bYear = request.form.get('Year')
            bType = request.form.get('Type')
            Loaned=request.form.get('Loaned')
            SQL=(f'''INSERT INTO Books VALUES("{bName}", "{bAuthor}", {int(bYear)}, {int(bType)}, "{Loaned}")''')
            print(SQL)
            if(bAuthor):
                if(len(bAuthor)>2):
                    cur.execute(SQL)
                    msg=f"The book ... {bAuthor} has been added to the list"
            con.commit()
            return render_template("/Books/addBook.html")
        return render_template("/Books/addBook.html")

    def removeBook(self):
        if request.method=='post':
            bName = request.args.get('Name')
            bookID = request.args.get('id')
            print(bookID)
            SQL=f'''DELETE FROM Books where rowid={bookID}'''
            cur.execute(SQL) 
            con.commit() 
            print(SQL)
            msg=f"The book ... {bName} has been removed from the list"
            return render_template("/Books/bookHomepage.html")
        return render_template("/Books/bookHomepage.html")

    # def updateBook(self):
    #     SQLUPD=f"UPDATE Books set Type=4 where rowid={bookID}"
    #     SQL=SQLUPD
    #     cur.execute(SQL) 
    #     con.commit()
    #     print(SQL)
    #     if request.method=='POST':
    #         return render_template("/Books/removeBook.html")

    def findBook(self):
        if request.method=='POST':
            bookName = request.form.get('bookName')
            sql = (f'''SELECT * FROM Books where Name like "%{bookName}%"''')
            cur.execute(sql)
            books = cur.fetchall()
            return render_template("/Books/findBooksByName.html",books=books)
        return render_template("/Books/findBooksByName.html")


    def bookHomepage(self):
        if request.method=='POST':
            pass
        allBooks = "SELECT * FROM Books"
        cur.execute(allBooks)
        books=cur.fetchall()
        return render_template("/Books/bookHomepage.html", foundbook=books)
       