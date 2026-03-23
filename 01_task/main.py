from fastapi import FastAPI, HTTPException
from models import tensorArrays
import torch

app = FastAPI()


@app.get("/")
def health():
    return {"message": "Server is working okay"}


@app.post("/add")
def addArrays(data: tensorArrays):
    mata = torch.tensor(data.mat1, dtype=torch.float32)
    matb = torch.tensor(data.mat2, dtype=torch.float32)

    if mata.shape != matb.shape:
        raise HTTPException(status_code=400, detail="Shape mismatch")

    result = mata + matb

    return {
        "result": result.tolist(),
        "shape": result.shape,
        "device": result.device,
        "dtype": result.dtype,
    }
