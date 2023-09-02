from pymongo import MongoClient
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash

mon = MongoClient('mongodb+srv://baniksuman918:roPM1OmnSOWKphLe@cluster0.fajm9ik.mongodb.net/')
db = mon['demo']
username = db['data']

def insert_data(request):
    if request.method == "POST":
        variable1 = generate_password_hash(request.form['new-password'])
        username.insert_many([request.form.get('first_name'),request.form.get('last_name'),request.form.get('new_email'), variable1])
        return True
    else:
        return False

def check_user(request):
    if request.method == "POST":
        u = username.find_one('first_name'==request.form['username'])
        hpassword = u.find_one('new-password')
        check_password_hash(hpassword, request.form['password'])
        return True
    else:
        return False