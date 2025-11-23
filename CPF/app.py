from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)

cpfs_validos = [] 

def validar_cpf(cpf):
    cpf = re.sub(r'[^0-9]', '', cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calc_digito(digs, pesos):
        soma = sum(int(d) * p for d, p in zip(digs, pesos))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    pesos1 = list(range(10, 1, -1))
    pesos2 = list(range(11, 1, -1))

    digito1 = calc_digito(cpf[:9], pesos1)
    digito2 = calc_digito(cpf[:9] + str(digito1), pesos2)

    return cpf[-2:] == f"{digito1}{digito2}"


@app.route("/")
@app.route("/validar", methods=["GET", "POST"])
def validar():
    resultado = None
    if request.method == "POST":
        cpf = request.form.get("cpf")
        if validar_cpf(cpf):
            if cpf not in cpfs_validos:
                cpfs_validos.append(cpf)
            resultado = f"O CPF {cpf} é válido."
        else:
            resultado = f"O CPF {cpf} é inválido."
    return render_template("validar.html", resultado=resultado, lista_cpfs=cpfs_validos)

if __name__ == "__main__":
    app.run(debug=True)