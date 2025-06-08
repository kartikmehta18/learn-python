from fastapi import FastAPI ,HTTPException
from pydantic import BaseModel
from typing import List


app = FastAPI()

class Tea(BaseModel):
    id:int
    name:str
    origin:str
    
teas:List[Tea] = []


@app.get("/")
def read_root():
    return {"message": "Welcome to the Tea API!"}

@app.get("/teas")
def get_teas():
    return teas

# @app.post("/teas")
# def add_tea(tea:Tea):
#     teas.append(tea)
#     return tea

@app.post("/teas")
def add_tea(tea: Tea):
    if any(t.id == tea.id for t in teas):
        raise HTTPException(status_code=400, detail="Tea with this ID already exists")
    teas.append(tea)
    return tea

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int,update_tea:Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] =update_tea
            return update_tea
        return {"error":"tea not found"}
    
@app.delete("/teas/{tea_id}")
def delete_tea(tea_id:int):
    for index, tea in enumerate(teas):
        if tea.id== tea_id:
           deleted = teas.pop(index)
           return deleted
    return {"error" :"Tea not found"}

# http://127.0.0.1:8000/docs
# uvicorn main:app --reload