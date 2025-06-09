from fastapi import FastAPI
import os
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Render API working!"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
