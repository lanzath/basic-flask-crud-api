# o pacote do sqlite3 deve ser substituído pelo pacote correspondente ao banco a ser utilizado (oracle, postgresql, mysql...)
import sqlite3, random, datetime

# importando a model book
from models import Book

# método para gerar um id
def getNewId():
    return random.getrandbits(28)

# seed de livros - para criar um banco que já possui dados
books = [
    # {
    #     'available': True,
    #     'title': 'Don Quixote',
    #     'timestamp': datetime.datetime.now()
    # },
    {
        'available': True,
        'title': 'A Tale of Two Cities',
        'timestamp': datetime.datetime.now()
    },
    {
        'available': True,
        'title': 'The Lord of the Rings',
        'timestamp': datetime.datetime.now()
    },
    {
        'available': True,
        'title': 'The Little Prince',
        'timestamp': datetime.datetime.now()
    },
    {
        'available': True,
        'title': "Harry Potter and the Sorcerer's Stone",
        'timestamp': datetime.datetime.now()
    },
    {
        'available': True,
        'title': 'And Then There Were None',
        'timestamp': datetime.datetime.now()
    },
    {
        'available': True,
        'title': 'The Dream of the Red Table',
        'timestamp': datetime.datetime.now()
    },
    {
        'available': True,
        'title': 'The Hobbit',
        'timestamp': datetime.datetime.now()
    },
    {
        'available': True,
        'title': 'The Lion, the Witch and the Wardrobe',
        'timestamp': datetime.datetime.now()
    },
    {
        'available': True,
        'title': 'The Da Vinci Code',
        'timestamp': datetime.datetime.now()
    },
]

# método para conectar-se ao db
def connect():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, available BOOLEAN, title TEXT, timestamp TEXT)")
    conn.commit() # executa o comando sql e "comita" (salva) as alterações
    conn.close() # sempre ao finalizar operações no DB é boa prática encerrar a conexão.
    for book in books:
        bk = Book(getNewId(), book['available'], book['title'], book['timestamp'])
        insert(bk)

# método para inserir um novo dado no DB
def insert(book):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (?,?,?,?)", (
        book.id,
        book.available,
        book.title,
        book.timestamp
    ))
    conn.commit()
    conn.close()

# método para listar livros
def get():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    books = []
    for i in rows:
        book = Book(i[0], True if i[1] == 1 else False, i[2], i[3])
        books.append(book)
    conn.close()
    return books

# método para consultar um livro por seu ID
def getById(id):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE id=?", (id,))
    row = cur.fetchone()
    if row:
        book = Book(row[0], bool(row[1]), row[2], row[3])
    else:
        book = None
    conn.close()
    return book

# método para atualizar um livro a partir de seu ID
def update(book):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("UPDATE books SET available=?, title=? WHERE id=?", (book.available, book.title, book.id))
    conn.commit()
    conn.close()

# método para deletar um livro do DB
def delete(theId):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?", (theId,))
    conn.commit()
    conn.close()

# método para deletar todos os livros do db
def deleteAll():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM books")
    conn.commit()
    conn.close()