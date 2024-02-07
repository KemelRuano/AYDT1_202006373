from flask import Flask , request

app = Flask(__name__)

@app.route('/AgregarCancion' , methods=['POST'])
def AgregarCancion():
    if request.method == 'POST':
        jsondate = request.get_json() 
    Detalle = jsondate.get('nombre') + ' | ' + jsondate.get('artista') + ' | ' + jsondate.get('genero') 
    return {'Cancion Agregada Correctamente' : Detalle }


@app.route('/VerCarnet' , methods=['GET'])
def VerCarnet():
    return {'Carnet' : 202006373}


if __name__ == '__main__':
    app.run(debug=True)