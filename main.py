from fastapi import FastAPI,status
from routers.book_router import book_router



app = FastAPI(
    title="Bookily",
    description="RSST api services for book review services",
    version="v1"
)
@app.get("/health")
async def get_health():
    return {"status":"OK"}
app.include_router(book_router,prefix="/api/v1/books",tags=["books api list"])