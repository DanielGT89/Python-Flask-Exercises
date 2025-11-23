from tensorflow.keras.models import load_model
from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

modeloIA = r'modelo.ia.diabetes.h5'
scalerIA = r'scaler.modelo.ia.diabetes.pkl'

modelo = load_model(modeloIA)
scaler = pickle.load(open(scalerIA, 'rb'))

@app.route('/')
def paginaInicial():
    return render_template('index.html')

@app.route('/previsao', methods=['POST'])
def previsaoDiagnostico():
    dadosPaciente = [
        float(request.form['genero']), float(request.form['idade']),
         float(request.form['hipertensao']), float(request.form['cardiaco']), 
        float(request.form['fumante']),  float(request.form['imc']), 
        float(request.form['hba1c']), float(request.form['glicose'])
        ]
    
    dadosPaciente = scaler.transform([dadosPaciente])
    
    probabilidade = modelo.predict(dadosPaciente)[0][0]
    
    if probabilidade >= 0.5:
        diagnostico = "Risco de Diabetes"
    else:
        diagnostico = "Sem Risco de Diabetes"
    
    probabilidade = f"{probabilidade * 100:.1f}"
    
    return render_template('index.html', previsao=diagnostico, probabilidade=probabilidade )

if __name__ == '__main__':
    app.run(debug=True)