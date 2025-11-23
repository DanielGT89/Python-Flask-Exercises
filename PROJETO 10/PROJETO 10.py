from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'daniel'  




@app.route('/')
def jogo():
    
    if 'numero_secreto' not in session:
        session['numero_secreto'] = random.randint(1, 100)
        session['tentativas'] = 0
    return render_template('jogo.html')

@app.route('/adivinhar', methods=['POST'])
def adivinhar():
    tentativa = int(request.form['tentativa'])
    session['tentativas'] += 1
    numero_secreto = session['numero_secreto']

    if tentativa < numero_secreto:
        mensagem = "Muito baixo! Tente um número maior."
    elif tentativa > numero_secreto:
        mensagem = "Muito alto! Tente um número menor."
    else:
        mensagem = f"Parabéns! Você acertou em {session['tentativas']} tentativas!"
        
        session.pop('numero_secreto', None)

    return render_template('resultado.html', 
                         mensagem=mensagem,
                         acertou=(tentativa == numero_secreto))

if __name__ == '__main__':
    app.run(debug=True)