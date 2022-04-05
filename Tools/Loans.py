from flask import redirect, render_template, request
import sqlite3


con=sqlite3.connect("Library.db", check_same_thread=False)
cur=con.cursor()

class Loans:
    def __init__(self):
        pass
