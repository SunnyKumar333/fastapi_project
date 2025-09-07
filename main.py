from fastapi import FastAPI,status
from contextlib import asynccontextmanager
from src.routers.book_router import book_router
from src.db.main import init_db


@asynccontextmanager
async def life_span(app:FastAPI):
    print("Starting the server....")
    await init_db()
    yield
    print("stopping the Server....")

app = FastAPI(
    title="Bookily",
    description="RSST api services for book review services",
    version="v1",
    lifespan=life_span
)
@app.get("/health")
async def get_health():
    return {"status":"OK"}
app.include_router(book_router,prefix="/api/v1/books",tags=["books api list"])