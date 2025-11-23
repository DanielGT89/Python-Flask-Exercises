from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def terreno():
    return render_template('terreno.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    largura_terreno = float(request.form['larguraterreno'])
    profundidade_terreno = float(request.form['profundidadeterreno'])
    largura_calcada = float(request.form['larguracalcada'])
    altura_concreto = float(request.form['alturaconcreto'])
    
    if altura_concreto < 1:
        altura_concreto *= 0.01
    
    if largura_calcada < 1.2:
        largura_calcada = 1.2
    if altura_concreto < 0.06:
        altura_concreto = 0.06
    
    area_calcada = largura_terreno * largura_calcada
    volume_concreto = area_calcada * altura_concreto
    
    return render_template('resultadoterreno.html',
                         larguraterreno=largura_terreno,
                         profundidadeterreno=profundidade_terreno,
                         larguracalcada=largura_calcada,
                         alturaconcreto=altura_concreto,
                         volumeconcreto=round(volume_concreto, 2))

if __name__ == '__main__':
    app.run(debug=True)