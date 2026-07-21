from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def raiz(nombre: str):
    return {"mensaje": f"¡Hola desde FastAPI! {nombre}"}

@app.post("/saludo")
def saludo(nombre: str):
    return {"mensaje": f"¡Hola, {nombre}!"}

@app.put("/actualizar")
def actualizar(nombre: str, nuevo_nombre: str):
    return {"mensaje": f"Nombre actualizado de {nombre} a {nuevo_nombre}"}

@app.delete("/eliminar")
def eliminar(nombre: str):
    return {"mensaje": f"Nombre {nombre} eliminado"}

@app.patch("/modificar")
def modificar(nombre: str, nuevo_nombre: str):
    return {"mensaje": f"Nombre modificado de {nombre} a {nuevo_nombre}"}
