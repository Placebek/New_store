
from flask import Flask, render_template, request, redirect, session
from business_logic.auth_business_logic import AuthBusinessLogic
from models.user import User


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    print("SESSION:   ", session["logged_in_user"])
    if session["logged_in_user"] != None:
        return render_template("index.html", user=session["logged_in_user"])

    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        login = request.form['login']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        datalar = {
            "login": login,
            "password": password,
            "first_name": first_name,
            "last_name": last_name
        }

        auth_business_logic = AuthBusinessLogic()
        login_successful = auth_business_logic.login_user(login=login, password=password)

        register_user = User()
        register_user.create_user(data = datalar)
        session["logged_in_user"] = "Жандарбек" # осы жерге user-дің first_name, last_name жолдарын жазу керек

        if login_successful == False:
            return render_template("login.html", error="Incorrect login or password")

        session["logged_in_user"] = "Жандарбек" # осы жерге user-дің first_name, last_name жолдарын жазу керек

        return redirect('/')

    return render_template("login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    pass


if __name__ == "__main__":
    app.run(debug=True)
