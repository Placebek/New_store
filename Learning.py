from flask import Flask, render_template, request, redirect
from Data import Dataaccessor, courses
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    bok = courses()
    bok.courses(table_name = 'courses')
    return render_template("index.html")



@app.route('/about', methods=['POST', 'GET'])
def about():
    if request.method == "POST":
        emailname = request.form['email']
        password = request.form['password']
        datalar = {
            'emailname': emailname,
            'password' : password
        }


        try:
            connect = Dataaccessor()
            connect.insert_data(table_name = 'books', data = datalar)
            return redirect('/home')
        except Exception as e:
            print(e)
            return 'Error'
    else:
        return render_template("about.html")

# @app.route('/about/home', methods=['POST', 'GET'])
# def about_home():
#     if request.method == 'POST':



if __name__ == "__main__":
    app.run(debug=True)
