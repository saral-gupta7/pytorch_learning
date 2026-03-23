from pydantic import BaseModel, Field


class tensorArrays(BaseModel):
    mat1: list[list[float]] = Field(..., description="Both matrices are required")
    mat2: list[list[float]] = Field(..., description="Both matrices are required")


class statArray(BaseModel):
    array: list[float]
