from fastapi import FastAPI, Form, Response
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir qualquer origem
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

app.title = "Primeira aplicação com o FastAPI"
app.version = '2.0.0'

# pegando todos os livros
@app.get("/", tags=['Home'])
def home():
    response = Response()
    response.headers["Access-Control-Allow-Origin"] = "*"
    from bd import read

    books = read.readBooks()
    return [{"book_name": book["book_name"], "year": book["year"], "book_author": book["book_author"],
            "book_pages": book["book_pages"], "book_ISNB": book["book_ISNB"]} for book in books]


# pegando livro pelo ISNB
@app.get('/book/')
def getBookISNB(book_ISNB: str = Form()):

    from bd import read

    book = read.readBookISNB(book_ISNB)

    if book:
        return book

    return HTMLResponse("<h1>Livro Não Encontrado</h1>")
    # return HTMLResponse("<h1>Livro Não Encontrado</h1><br><a href='/'>Voltar Para o Início</a>")


# pegando livros por titulo
@app.get('/books/title/')
def getBooksTitle(book_name: str = Form()):

    from bd import read

    books = read.readBooksTitle(book_name)

    if books:
        return [{"book_name": book["book_name"], "year": book["year"], "book_author": book["book_author"],
          "book_pages": book["book_pages"], "book_ISNB": book["book_ISNB"]} for book in books]


# pegando livros por ano
@app.get('/books/year/')
def getBooksYear(year: str = Form()):

    from bd import read

    books = read.readBooksYear(year)

    if books:
        return [{"book_name": book["book_name"], "year": book["year"], "book_author": book["book_author"],
          "book_pages": book["book_pages"], "book_ISNB": book["book_ISNB"]} for book in books]

    return HTMLResponse("<h1>Livro Não Encontrado</h1>")


# pegando livros por autor
@app.get('/books/author/')
def getBooksAuthor(book_author: str = Form()):

    from bd import read

    books = read.readBooksAuthor(book_author)

    if books:
        return [{"book_name": book["book_name"], "year": book["year"], "book_author": book["book_author"],
          "book_pages": book["book_pages"], "book_ISNB": book["book_ISNB"]} for book in books]

    return HTMLResponse("<h1>Livro Não Encontrado</h1>")


# Atualizar Livro
@app.put("/edit/livro")
def editBook(book_ISNB: str = Form()):

    pass


# Adicionar Livro
@app.post("/add/book/")
def addBook(book_name: str = Form(), year: str = Form(), book_author: str = Form(), book_pages: str = Form(), book_ISNB: str = Form()):
    from bd import create

    create.addBook(book_name, year, book_author, book_pages, book_ISNB)

    return HTMLResponse("<h1>Livro Adicionado com Sucesso.</h1>")


# deletando livro
@app.delete('/book/delete/')
def deleteBook(book_ISNB: str = Form()):

    from bd import delete

    book_delete = delete.deleteBook(book_ISNB)

    if book_delete:
        return HTMLResponse("<h1>Livro Deletado Com Sucesso.</h1>")

    return HTMLResponse("<h1>Livro Não Encontrado.</h1>")

    pass

if __name__ == '__main__':
    import uvicorn
    print(">>>>>>>>>>>> version V0.0.1")
    uvicorn.run(app, host="0.0.0.0", port=8000)