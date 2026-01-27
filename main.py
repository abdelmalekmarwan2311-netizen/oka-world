from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# الجزء ده هو اللي بيخلي المتصفح يوافق يكلم السيرفر
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # بيسمح لأي موقع بالوصول
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/f40-info")
def get_f40():
    return {
        "model": "Ferrari F40",
        "engine": "2.9 L twin-turbocharged V8",
        "top_speed": "324 km/h (201 mph)",
        "description": "The Ferrari F40 is a mid-engine, rear-wheel drive sports car."
    }