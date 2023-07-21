from flask import Flask, jsonify, request

#DEFINES THE APP NAME
app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Lógica de Programação e Algorítmos com JS',
        'autor': 'Edécio Fernando Iepsen',
    },
    {
        'id': 2,
        'titulo': 'Lógica de Programação e Algorítmos com Python',
        'autor': 'Edécio Fernando Iepsen',
    },
    {
        'id': 3,
        'titulo': 'Lógica de Programação e Algorítmos com C#',
        'autor': 'Edécio Fernando Iepsen',
    }
]

#GET ALL BOOKS LIST
@app.route('/livros', methods=['GET'])
def getBooks():
    return jsonify(livros)

#GET BOOK BBY ID
@app.route('/livros/<int:id>', methods=['GET'])
def getBookById(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

##STARTUP
app.run(port=5000,host='localhost', debug=True)