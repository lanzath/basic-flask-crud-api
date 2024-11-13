# Model é uma classe que representará uma tabela de um banco de dados.
class Book:
  # __init__ é o método "construtor" do python
  def __init__(self, id, available, title, timestamp):
    self.id = id # self é equivalente ao "this" em linguagens como java, c#, etc...
    self.title = title
    self.available = available
    self.timestamp = timestamp

  def __repr__(self):
    return '<id {}>'.format(self.id)

  def serialize(self):
    return {
      'id': self.id,
      'title': self.title,
      'available': self.available,
      'timestamp':self.timestamp
    }