from flask import Flask, render_template, request
from regresion import prediccion, recomendar_jugo
import openai

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def inicio():
    pred = 0
    jugo_recomendado = ''

    if request.method == 'POST':
        # Eliminar jugo si quieres quitar el selector de jugo
        Jugo = request.form['Jugo']
        Textura = request.form['Textura']
        Sabor = request.form['Sabor']

        pred = prediccion(int(Jugo), int(Textura), int(Sabor))[0]
        jugo_recomendado = recomendar_jugo(pred)
    return render_template('index.html', pred=pred, jugo_recomendado=jugo_recomendado)




















data=[]
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        message = request.form['message']
        response = generate_response(message)
        return render_template('chat.html', message=message, response=response, data=data)
    else:
        return render_template('chat.html')


openai.api_key = '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'

def generate_response(message):
    completion = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=3097,
        n=1,
        stop=None,
        temperature=0.2
    )
    response ="IA: "+ completion.choices[0].text.strip()
    data.append(message)
    data.append(response)
    return response, data

if __name__ == '__main__':
    app.run(debug=True)
