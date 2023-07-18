from flask import Flask, render_template

app = Flask(__name__, template_folder="..\Controlador-de-gastos-web\templates")
app.config(debug=True)

@app.route("/")
def homepage():
    return render_template("index.html")
