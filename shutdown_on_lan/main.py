from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/shutdown")
async def GetShutdown():
    Shutdown()
    return {"message": "I'm sleeping"}

def Shutdown():
    os.system("shutdown /s /t 5 /c \"Il sistema verrà spento tra 5 secondi\"")