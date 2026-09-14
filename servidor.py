from ia_tradutora import cadeia_dinamica
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI(title="IA Tradutora", description="API para tradução de texto usando IA", version="1.0.0")
add_routes(app, cadeia_dinamica, path="/tradutor")
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)