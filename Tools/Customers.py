from flask import render_template, request
import sqlite3
con=sqlite3.connect("Library.db", check_same_thread=False)
cur=con.cursor()

class Customers:
    def __init__(self):
        pass

    def myCustomer(self):
        SQL=(f'''SELECT rowid, Name, Age, City FROM Customers''')
        print(SQL)
        res= []
        for i in cur.execute (SQL):
            res.append({"id": i[0], "Name": i[1], "Age": i[2], "City": i[3]})
        return render_template("/Customers/allCustomers.html", customers=res)

    def addCustomers(self):
        if request.method=='POST':
            custName = request.form.get('Name')
            custCity = request.form.get('City')
            custAge = request.form.get('Age')
            cur.execute(f'''INSERT INTO Customers VALUES(not null, "{custName}", "{custCity}", {int(custAge)})''')
            con.commit()
            return render_template("/Customers/CustHompage.html")
        return render_template("/Customers/CustHomepage.html")

    def removeCustomers(self):
        if request.method=='POST':
            custName = request.form.get('Name')
            sqlRemove = (f'''DELETE FROM Customers where Name="{custName}"''')
            cur.execute(sqlRemove)
            con.commit()
            sqlRemove="The selected Customer has been removed"
        return render_template("/Customers/allCustomers.html")
        

    def displayCustomers(self):
        if request.method=='POST':
            pass
        sqlCustomers = '''SELECT * FROM Customers'''
        cur.execute(sqlCustomers)
        customers = cur.fetchall()
        return render_template("/Customers/displayCustomers.html", customers=customers)
    
    def findCustomers(self):
        if request.method=="POST":
            custName=request.form.get("custName")
            findCust = (f'''SELECT * FROM Customers where Name like "%{custName}%" ''')
            cur.execute(findCust)
            cust = cur.fetchall()
            return render_template("/Customers/findCustomersByName.html", cust=cust)
        return render_template("/Customers/findCustomersByName.html")
