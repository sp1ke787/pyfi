from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def health_check():
    return {"msg": "success"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
