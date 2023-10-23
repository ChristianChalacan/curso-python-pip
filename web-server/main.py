import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return [1,2,3,5,6]

@app.get("/contact")
def get_contact():
    return {'name':'Christian'}

@app.get("/html", response_class = HTMLResponse)
def get_html():
    return"""
        <h1>Hola soy una pagina</h1>
        <p>Este es un parrafo base</p>
    """

def run():
    store.get_categories()
    
if __name__ == '__main__':
    run()