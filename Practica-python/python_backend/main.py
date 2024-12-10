## API REST: Interfazr de programacion de aplicaciones para compartir recursos
from typing import List, Optional
import uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Iniciamos varibale apirest
app = FastAPI()


# definimos modelo
class Curso(BaseModel):
    id: Optional[str] = None
    nombre: str
    description: Optional[str] = None
    nivel: str
    duration: int


# simular base de datos
cursos_db = []


### CRUD
# - READ
@app.get("/cursos/", response_model=List[Curso])
def obtener_cursos():
    return cursos_db


# - CREATE
@app.post("/cursos/", response_model=Curso)
def crear_curso(curso: Curso):
    curso.id = str(uuid.uuid4())
    cursos_db.append(curso)
    return curso


# - GET/:id
@app.get("/cursos/{curso_id}", response_model=Curso)
def obtener_curso(curso_id: str):
    curso = next((curso for curso in cursos_db if curso.id == curso_id), None)

    if curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return curso


# - UPDATE
@app.put("/cursos/{curso_id}", response_model=Curso)
def actualizar_curso(curso_id: str, curso_actualizado: Curso):
    curso = next((curso for curso in cursos_db if curso.id == curso_id), None)
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    curso_actualizado.id = curso_id
    index = cursos_db.index(curso)
    cursos_db[index] = curso_actualizado
    return curso_actualizado


# - DELETE
@app.delete("/cursos/{curso_id}", response_model=Curso)
def eliminar_curso(curso_id: str):
    curso = next((curso for curso in cursos_db if curso.id == curso_id), None)

    if curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    cursos_db.remove(curso)
    return curso