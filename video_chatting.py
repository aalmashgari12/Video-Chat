from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/abc')
def hello():
    return 'hello'


@app.route('/', methods = ['GET'])
def bye():
    return render_template('newform.html')


@app.route("/signin", methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        print(request.form)
        f = request.files['profile_picture']
        f.save(secure_filename(f.filename))
        return "Data saved!!"

        

if __name__ == '__main__':
    app.run()