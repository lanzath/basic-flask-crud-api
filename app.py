from flask import Flask, request, jsonify
import os, datetime
import db
from models import Book

app = Flask(__name__)

# create the database and table. Insert 10 test books into db
# Do this only once to avoid inserting the test books into
# the db multiple times
if not os.path.isfile('books.db'):
    db.connect()

@app.route("/books", methods=['POST'])
def postRequest():
    req_data = request.get_json()
    title = req_data['title']
    bks = [b.serialize() for b in db.get()]
    for b in bks:
        if b['title'] == title:
            return jsonify({
                'data': f'Error Book with title {title} is already in library!',
            }), 422
    bk = Book(db.getNewId(), True, title, datetime.datetime.now())
    db.insert(bk)
    return jsonify({
                'data': bk.serialize(),
            }), 201

@app.route('/books', methods=['GET'])
def getRequest():
    bks = [b.serialize() for b in db.get()] # Pega os livros retornados na consulta e serializa para json.
    return jsonify({
                'data': bks,
                'total': len(bks)
            }), 200

@app.route('/books/<id>', methods=['GET'])
def getRequestById(id):
    bk =  db.getById(id)
    if bk:
        return jsonify({
            'data': bk.serialize(),
        }), 200
    else:
        return jsonify({
            'error': f"Book with id '{id}' was not found!"
        }), 404

@app.route("/books/<id>", methods=['PUT'])
def putRequest(id):
    req_data = request.get_json()
    availability = req_data['available']
    title = req_data['title']
    bk = db.getById(id)
    if bk:
        bk = Book(id, availability, title, datetime.datetime.now())
        db.update(bk)
        return jsonify({
          'data': bk.serialize()
        }), 200
    else:
      return jsonify({
                'message': f'Error Failed to update Book with title: {title}!',
            }), 404

@app.route('/books/<id>', methods=['DELETE'])
def deleteRequest(id):
    bk = db.getById(id)
    if not id:
        return jsonify({
            'error': f"Error No Book ID sent!"
        }), 400
    if bk:
        db.delete(id)
        return jsonify({}), 204
    else:
        return jsonify({
            'error': f"Book with id '{id}' was not found!"
        }), 404

if __name__ == '__main__':
    app.run() # Base uri http://127.0.0.1:5000