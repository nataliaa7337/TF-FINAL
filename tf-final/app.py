import flask
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('home-banking.html')

@app.route('/procesar_gastos', methods=['POST'])
def procesar_gastos():
    pass

@app.route('/procesar_transferencias', methods=['POST'])
def procesar_transferencias():
    pass

@app.route('/proceso')
def proceso():
    return render_template('proceso.html')

@app.route('/procesar_depositos', methods=["POST"])
def procesar_depositos():
    file = request.files['file']
    return ''

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000, debug=True)