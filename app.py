from flask import Flask, request, jsonify, render_template, make_response
from flask_talisman import Talisman
from geoidear import Geoidear
import json

app = Flask(__name__)
Talisman(app, content_security_policy={
     'default-src': [
         '\'self\'',
         'https://fonts.googleapis.com',
         'https://fonts.gstatic.com'            
        ]
})

# add UTF-8 support:
app.config['JSON_AS_ASCII'] = False

@app.route('/', methods=['GET'])
def root():
    return render_template('index.html', version = '0.0.1')

@app.route('/convert', methods=['POST'])
def convert():
    try :
        data = request.form.get('data')
              
        if not data:
            return jsonify({"message":"No se envió información"}), 400

        epsg = 'EPSG:4326' if not "epsg" in request.form else request.form.get('epsg')
        
        responseType = 'json' if not "responseType" in request.form else request.form.get('responseType')

        geoidear = Geoidear(data, epsg)
        result = geoidear.processList()
        
        if responseType == 'csv':
            output = make_response(createStringFromList(result), 200)
            output.headers["Content-Disposition"] = "attachment; filename=geoidear-api.csv"
            output.headers["Content-type"] = "text/csv; charset=utf-8"
            return output

        elif responseType == 'text':
            result = createStringFromList(result)
            return jsonify(result)

        else:
            return jsonify(result)
        
    except Exception as e:
        return jsonify({"message":"Ocurrió un error al procesar. " + str(e)}), 500


def createStringFromList(data):
    dataString = 'Latitud , Longitud , Elev (metros)\n'
    for line in data:
        dataString += ",".join( str(i) for i in line )
        dataString += '\n'
    return dataString

if __name__ == '__main__':
    app.run()