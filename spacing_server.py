from fastapi import FastAPI, Request
from pydantic import BaseModel
from pykospacing import Spacing

app = FastAPI()
spacing = Spacing()

class TextRequest(BaseModel):
    text: str

@app.post("/spacing")
def spacing_endpoint(req: TextRequest):
    corrected = spacing(req.text)
    return {"result": corrected}
