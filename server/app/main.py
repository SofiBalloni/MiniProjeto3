from flask import Flask, request, jsonify

app = Flask(__name__)

livros = []
id_livro = 1


@app.route('/api/v1/livros', methods=['GET'])
def listar_livros():
    return jsonify(livros)


@app.route('/api/v1/livro', methods=['POST'])
def criar_livro():
    global id_livro
    data = request.get_json()
    data['id'] = id_livro
    id_livro += 1
    livros.append(data)
    return jsonify({'mensagem': 'Livro cadastrado com sucesso!', 'livro': data}), 201


@app.route('/api/v1/livro', methods=['PUT'])
def atualizar_livro():
    data = request.get_json()
    for livro in livros:
        if livro['id'] == data['id']:
            livro.update({
                'titulo': data.get('titulo', livro['titulo']),
                'autor': data.get('autor', livro['autor']),
                'ano': data.get('ano', livro['ano'])
            })
            return jsonify({'mensagem': 'Livro atualizado com sucesso!', 'livro': livro}), 200
    return jsonify({'erro': 'Livro não encontrado'}), 404


@app.route('/api/v1/livro', methods=['DELETE'])
def deletar_livro():
    global livros
    data = request.get_json()
    livros = [livro for livro in livros if livro['id'] != data['id']]
    return jsonify({'mensagem': 'Livro removido com sucesso!'}), 200


if __name__ == '__main__':
    app.run(debug=True)
