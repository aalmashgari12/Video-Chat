from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from db import insert_data, check_user
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/abc')
def hello():
    return 'hello'

os.environ['app_id'] = 'e22356a363ec46a4b0235693b4ab5d38'
os.environ['primary_certificate'] = 'eb8f05d416e443ee89943c2e5b942e15'

@app.route('/', methods = ['GET'])
def bye():
    return render_template('newform.html')


@app.route("/signin", methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
       if check_user(request) == True: 
        return 'Login successful'
        # f = request.files['profile_picture']
        # f.save(secure_filename(f.filename))
       else:
        return 'Login failed'

@app.route("/signup", methods = ['POST','GET'])
def register():  
    if request.method == 'POST':
        if insert_data(request) == True:
            return "Username is saved"
        else:
            return "Username was not saved"

@app.route("/home", methods = ['POST','GET'])
def home_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)