# CRUD Básico de livros feito em python 3 e flask

> Exemplo básico de REST API com CRUD para cadastro, consulta, edição e deleção de livros.

## Referências

- https://www.python.org/
- https://flask.palletsprojects.com/en/stable/
- https://www.sqlite.org/
- https://medium.com/@hillarywando/how-to-create-a-basic-crud-api-using-python-flask-cd68ef5fd7e3


##### Exemplo de payload para método POST
```json
{
  "title": "O Silmarillion",
  "available": 1
}
```

##### Exemplo de response para GET
```json
{
  "data": [
    {
      "available": true,
      "id": 158751347,
      "timestamp": "2024-11-12 19:53:47.534073",
      "title": "Harry Potter and the Sorcerer's Stone"
    },
    {
      "available": true,
      "id": 195446472,
      "timestamp": "2024-11-12 19:53:47.534071",
      "title": "The Lord of the Rings"
    }
  ],
  "total": 8
}
```

##### Exemplo de response para GET BY ID
```json
{
  "data": {
    "available": true,
    "id": 158751347,
    "timestamp": "2024-11-12 19:53:47.534073",
    "title": "Harry Potter and the Sorcerer's Stone"
  }
}
```