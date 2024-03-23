from flask import Flask, render_template, request, redirect, session
from business_logic.auth_business_logic import AuthBusinessLogic


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
        email = request.form['email']
        phone_number = request.form['phone_number']
        password = request.form['password']
        
        

        auth_business_logic = AuthBusinessLogic()

        
       
        

        login_successful = auth_business_logic.login_user(email=email, password=password)
        if login_successful == False:
            return render_template("login.html", error="Incorrect login or password")
        
        name_successful = auth_business_logic.register_user(email=email, password=password, phone_number=phone_number)
        if name_successful == False:
            return render_template("login.html", error="Ваш номер телефона не корректный")

        
        

        # session["logged_in_user"] = first_name



        return redirect('/')

    return render_template("login.html")


@app.route('/products', methods=['GET', 'POST'])
def post_products():
    if request.method == "POST":



        return redirect('/')

    return render_template("product.html")



if __name__ == "__main__":
    app.run(debug=True)
