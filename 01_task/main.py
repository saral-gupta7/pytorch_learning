from fastapi import FastAPI, HTTPException, status
from models import tensorArrays, statArray
import torch

app = FastAPI()


@app.get("/")
def health():
    return {"message": "Server is working okay"}


@app.post("/add", status_code=status.HTTP_201_CREATED)
def addArrays(data: tensorArrays) -> dict:
    mata = torch.tensor(data.mat1, dtype=torch.float32)
    matb = torch.tensor(data.mat2, dtype=torch.float32)

    if mata.shape != matb.shape:
        raise HTTPException(status_code=400, detail="Shape mismatch")

    result = mata + matb

    return {"result": result.tolist(), **tensor_metadata(result)}


@app.post("/matmul", status_code=status.HTTP_201_CREATED)
def multiplyArray(data: tensorArrays) -> dict:
    mata = torch.tensor(data.mat1, dtype=torch.float32)
    matb = torch.tensor(data.mat2, dtype=torch.float32)
    if mata.shape[1] != matb.shape[0]:
        raise HTTPException(
            status_code=400,
            detail=f"Incompatible shapes for matmul: {list(mata.shape)} @ {list(matb.shape)} — inner dims {mata.shape[1]} and {matb.shape[0]} must match",
        )
    product = torch.matmul(mata, matb)

    return {"result": product.tolist(), **tensor_metadata(product)}


@app.post("/stats", status_code=status.HTTP_201_CREATED)
def stats(arrayItem: statArray) -> dict:
    array_tensor = torch.tensor(arrayItem.array, dtype=torch.float32)

    mean = torch.mean(array_tensor)
    median = torch.median(array_tensor)
    minItem = torch.min(array_tensor)
    maxItem = torch.max(array_tensor)
    return {
        "mean": mean.item(),
        "median": median.item(),
        "min": minItem.item(),
        "max": maxItem.item(),
    }


def tensor_metadata(data: torch.Tensor) -> dict:
    return {
        "shape": list(data.shape),
        "device": str(data.device),
        "dtype": str(data.dtype),
    }
