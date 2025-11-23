from flask import Flask, render_template, request,  url_for, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return redirect(url_for("home"))


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/cadastrado", methods=["GET", "POST"])
def cadastrado():
    nome = ""
    email = ""
    telefone = ""
    senha = ""
    
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        telefone = request.form.get("telefone")
        senha = request.form.get("senha")
        
    return render_template("cadastrado.html", nome=nome, email=email, telefone=telefone)

if __name__ == "__main__":
    app.run(debug=True)
