
from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)

cnpj_valido = [] 


import re

def validar_cnpj(cnpj: str) -> bool:
    cnpj = re.sub(r'\D', '', cnpj)  

    if len(cnpj) != 14:
        return False

    if cnpj == cnpj[0] * 14:
        return False  

    def calcular_digito(cnpj_parcial):
        if len(cnpj_parcial) == 12:
            pesos = [5,4,3,2,9,8,7,6,5,4,3,2]
        elif len(cnpj_parcial) == 13:
            pesos = [6,5,4,3,2,9,8,7,6,5,4,3,2]
        else:
            return None

        soma = 0
        for i in range(len(cnpj_parcial)):
            soma += int(cnpj_parcial[i]) * pesos[i]

        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    digito1 = calcular_digito(cnpj[:12])
    digito2 = calcular_digito(cnpj[:12] + digito1)

    return cnpj[-2:] == digito1 + digito2


@app.route("/")
@app.route("/validar", methods=["GET", "POST"])
def validar():
    resultado = None
    if request.method == "POST":
        cnpj = request.form.get("cnpj")
        if validar_cnpj(cnpj):
            if cnpj not in cnpj_valido:
                cnpj_valido.append(cnpj)
            resultado = f"O CNPJ {cnpj} é válido."
        else:
            resultado = f"O CNPJ {cnpj} é inválido."
    return render_template("validar.html", resultado=resultado, lista_cnpjs=cnpj_valido)

if __name__ == "__main__":
    app.run(debug=True)
