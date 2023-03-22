from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/callname/{name}")
def get_name(name_id: int):
    return {"hello": {__name__}}


@app.post("/callname")
def post_name():
    return {"hello": {__name__}}

handler = Mangum(app)