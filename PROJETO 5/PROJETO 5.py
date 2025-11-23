from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)



@app.route("/")
def index():
    return redirect(url_for("home"))



def medicoesterreno(largura, comprimento):
    area = largura*comprimento
    perimentro = 2 *largura + 2* comprimento
    return area, perimentro  

@app.route("/home")
def home():
    return render_template("home.html") 

 

@app.route("/calculoterreno", methods=["GET", "POST"])
def calculoterreno():

    if request.method ==  "POST":
        largura = float(request.form.get("largura"))
        comprimento = float(request.form.get("comprimento"))

        area, perimetro = medicoesterreno(largura, comprimento)

        return render_template("calculoterreno.html", largura=largura, comprimento=comprimento, area=area, perimetro=perimetro)
       

if __name__ == "__main__":
    app.run(debug=True)  
