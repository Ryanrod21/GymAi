from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Gym Coach API running!"}

@app.get("/workout")
async def generate_workout(query: str):
    # Call your GymManager here
    return {"workout": f"Generated plan for: {query}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        reload=False
    )
