import api_data
import uvicorn
from fastapi import FastAPI
from models.Character_Model import CharacterModel as model


app= FastAPI()

@app.get("/")
async def index():
    return{
        "Bienvenido al repositorio de yapo!",
        "Para realizar la busqueda cambiar el parametro a /products/id",
        "ESTO ES SOLO USO ADMINISTRATIVO"
    }


@app.get("/products/{id}", response_model=model)
async def characterGetter(id:int):
    character=await api_data.get_characterById(id)
    return character.dict()

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0",port=80)




