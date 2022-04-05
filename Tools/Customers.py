from flask import render_template, request
import sqlite3
con=sqlite3.connect("Library.db", check_same_thread=False)
cur=con.cursor()

class Customers:
    def __init__(self):
        pass

    def addCustomers(self):
        if request.method=='POST':
            custName = request.form.get('custName')
            custCity = request.form.get('custCity')
            custAge = request.form.get('custAge')
            cur.execute(f'''INSERT INTO Customers VALUES(not null, "{custName}", "{custCity}", {int(custAge)})''')
            con.commit()
        return render_template("/Customers/addCustomer.html")
    
    def removeCustomers(self):
        if request.method=='POST':
            custName = request.form.get('custName')
            custCity = request.form.get('custCity')
            custAge = request.form.get('custAge')
            sqlRemove = (f'''DELETE FROM Customers where cusName="{custName}" and cusCity="{custCity}" and cusAge={int(custAge)}''')
            cur.execute(sqlRemove)
            con.commit()
            sqlRemove="The selected Customer has been removed"
        return render_template("/Customers/removeCustomer.html")

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
            custCity=request.form.get("custCity")
            findCust = (f'''SELECT * FROM Customers where cusName like "%{custName}%" and cusCity like "%{custCity}%"''')
            cur.execute(findCust)
            cust = cur.fetchall()
            return render_template("/Customers/findCustomer.html", cust=cust)
        return render_template("/Customers/findCustomer.html")
