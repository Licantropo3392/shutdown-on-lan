from fastapi import FastAPI
import uvicorn
import os
import argparse

app = FastAPI()

parser = argparse.ArgumentParser(description="Shutdown On Lan")
parser.add_argument("--port", type=int, default=8000, help="Port to run the FastAPI app on")
parser.add_argument("--message", type=str, default="The system will shut down in 5 seconds", help="Shutdown message")
parser.add_argument("--hide-message", action='store_true', help="Hide shutdown message")
args = parser.parse_args()

@app.get("/shutdown")
async def GetShutdown():
    Shutdown(args.message, args.hide_message)
    return {"message": args.message}

def Shutdown(message, hide_message):
    if hide_message:
        os.system("shutdown /s /t 5")
    else:
        os.system(f"shutdown /s /t 5 /c \"{message}\"")

def main():
    uvicorn.run(app, host="0.0.0.0", port=args.port)

if __name__ == "__main__":
    main()