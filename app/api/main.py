from fastapi import FastAPI

app = FastAPI(title="AI Technical Interview Coach")


@app.get("/")
def home():
    return {
        "message": "AI Technical Interview Coach API is running!"
    }