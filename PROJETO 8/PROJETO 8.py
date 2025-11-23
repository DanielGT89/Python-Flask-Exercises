from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade Grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade Grau 2"
    else:
        return "Obesidade Grau 3 (Mórbida)"

@app.route('/')
def calcular():
    return render_template('calcular.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    nome = request.form['nome']
    idade = request.form['idade']
    peso = float(request.form['peso'])
    altura = float(request.form['altura'])

    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)

    return render_template('resultado.html', nome=nome, idade=idade, peso=peso, altura=altura, imc=imc, classificacao=classificacao)

if __name__ == '__main__':
    app.run(debug=True)
