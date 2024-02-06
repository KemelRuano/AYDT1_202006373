from flask import Flask , request

app = Flask(__name__)

@app.route('/AgregarCancion' , methods=['POST'])
def AgregarCancion():
    if request.method == 'POST':
        jsondate = request.get_json() 
    Detalle = jsondate.get('nombre') + ' | ' + jsondate.get('artista') + ' | ' + jsondate.get('album') 
    return {'Cancion Agregada Correctamente' : Detalle }

if __name__ == '__main__':
    app.run(debug=True)