from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

@app.get("/shutdown")
async def GetShutdown():
    Shutdown()
    return {"message": "I'm sleeping"}

def Shutdown():
    os.system("shutdown /s /t 5 /c \"Il sistema verrà spento tra 5 secondi\"")

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()