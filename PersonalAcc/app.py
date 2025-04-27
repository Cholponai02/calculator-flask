from  flask import Flask, render_template, request, redirect,url_for
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

users = {
    "test@gmail.com":"1234",
    "cholponay112@gmail.com":"5678"
}

@app.route("/login", methods=['GET', 'POST']) #это путь
def login():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users and users[email] == password:
            return redirect(url_for('welcome'))
        else:
            error = "Неверный логин или пароль"
    return render_template("login.html", error=error)

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

history=[]
@app.route("/calculator", methods=["GET","POST"])
def calculator():
    expression = ""
    result = ""
    if request.method == 'POST':
        expression = request.form.get("expression","")
        button = request.form.get("button","")

        if button == "AC":
            expression = ""
        elif button == "=":
            try:
                result = str(eval(expression))
                history.append(f"{expression} = {result}")
                expression = result
            except:
                result="Ошибка"
                history.append(f"{expression} = ошибка")
                expression = ""
        else:
            expression = expression + button
            result = expression
    return render_template("calculator.html",result=result,expression=expression, history=history)

if __name__ == "__main__":
    app.run(debug=True)