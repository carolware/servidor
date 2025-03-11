from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'login' not in data or 'senha' not in data:
        return jsonify({'erro': 'Campos login e senha são obrigatórios'}), 400
    
    return jsonify({'login': data['login'], 'senha': data['senha']}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
