from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/LIVROS'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Livro(db.Model):
    __tablename__ = 'livros' 
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    ano = db.Column(db.String(4), nullable=False)
    dado = db.Column(db.String(150), nullable=False)
    ativo = db.Column(db.Boolean, default=True)
@app.route("/")
def index():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/catalago", methods=["GET", "POST"])
def catalago():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        autor = request.form.get("autor")
        ano = request.form.get("ano")
        dado = request.form.get("dado")

        novo_livro = Livro(titulo=titulo, autor=autor, ano=ano, dado=dado)
        db.session.add(novo_livro)
        db.session.commit()

        return render_template("catalago.html", titulo=titulo, autor=autor, ano=ano, dado=dado)
    return redirect(url_for("home"))

@app.route("/livros")
def livros():
    lista = Livro.query.filter_by(ativo=True).all()  
    return render_template("livros.html", livros=lista)

@app.route("/desativar/<int:id>")
def desativar(id):
    livro = Livro.query.get_or_404(id)
    livro.ativo = False
    db.session.commit()
    return redirect(url_for("livros"))


@app.route("/pesquisar", methods=["GET", "POST"])
def pesquisar():
    resultados = []
    termo = ""
    
    if request.method == "POST":
        termo = request.form.get("termo")

        
        resultados = Livro.query.filter(
            Livro.ativo == True,
            db.or_(
                Livro.titulo.ilike(f"%{termo}%"),
                Livro.autor.ilike(f"%{termo}%"),
                Livro.ano.ilike(f"%{termo}%"),
                Livro.dado.ilike(f"%{termo}%")
            )
        ).all()

    return render_template("pesquisa.html", resultados=resultados, termo=termo)




if __name__ == "__main__":
    app.run(debug=True)
