from fastapi import FastAPI
import uvicorn
import auth.router as auth_router
import projects.router as projects_router
import tasks.router as tasks_router

app = FastAPI()

app.include_router(auth_router.router)
app.include_router(projects_router.router)
app.include_router(tasks_router.router)

@app.get("/",tags=["root"])
async def root():
    return {"message":"Heeeess baaaack"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

