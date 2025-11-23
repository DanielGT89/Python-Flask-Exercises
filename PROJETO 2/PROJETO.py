from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)



@app.route("/")
def index():
    return redirect(url_for("home"))


@app.route("/home")
def home():
    return render_template("home.html")  


@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")  

@app.route("/relatorio")
def relatorio():
    return render_template("relatorio.html")  

@app.route("/contato")
def contato():
    return render_template("contato.html") 

if __name__ == "__main__":
    app.run(debug=True)  
