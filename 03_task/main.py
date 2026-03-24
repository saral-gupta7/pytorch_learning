from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from stream import train

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://your-frontend-domain.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/train")
def trained_data(lr: float = 0.1):
    return StreamingResponse(train(lr=lr), media_type="text/event-stream")
