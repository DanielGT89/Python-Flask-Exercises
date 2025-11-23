from flask import Flask, render_template, redirect, url_for, request

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

@app.route("/novocadastro", methods=["GET", "POST"])
def novocadastro():

    if request.method ==  "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        telefone = request.form.get("telefone")
         
        return render_template("novocadastro.html", nome=nome, email=email, telefone=telefone)




@app.route("/relatorio")
def relatorio():
    return render_template("relatorio.html")  

@app.route("/contato")
def contato():
    return render_template("contato.html") 

if __name__ == "__main__":
    app.run(debug=True)  
