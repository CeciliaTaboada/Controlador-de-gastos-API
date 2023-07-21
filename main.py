from flask import Flask, render_template

app = Flask(__name__, template_folder="..\Controlador-de-gastos-web\\templates", static_folder="..\Controlador-de-gastos-web\static")

@app.route("/")
def homepage():
    return render_template("index.html")

