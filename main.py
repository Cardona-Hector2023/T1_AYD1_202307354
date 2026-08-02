from fastapi import FastAPI

app = FastAPI(title="API REST AYD1")

@app.get("/")
def read_root():
    return {"mensaje": "API funcionando correctamente"}

@app.get("/cancionFavorita")
def get_cancion_favorita():
    return {
        "nombre": "Hector Antonio Cardona Cos",
        "carnet": "202307354",
        "cancion_favorita": "18 Months",
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)