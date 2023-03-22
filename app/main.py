from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/callname/{name}")
def get_name(name: str = None):
    return {"hello": name}


@app.post("/callname")
def post_name(name="junior"):
    return {"hello": name}

handler = Mangum(app)
