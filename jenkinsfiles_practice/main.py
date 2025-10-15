from flask import flask, jsonify, request

app = flask(__name__)

@app.route('/hello',mmethods =['GET'])
def helloworld():
    if(request.method == 'GET'):
        data = {"data":"this is dockerfile creation by using python"}
        return jsonify(data)

if __name__ == ' __main__':
    app.run(host='0.0.0.0',port=9003)