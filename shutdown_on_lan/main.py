from ast import arg
from fastapi import FastAPI
import threading

from shutdown_on_lan import Arguments
from shutdown_on_lan import Tray
from shutdown_on_lan.Shutdown import Shutdown
from shutdown_on_lan.Server import Server

app = FastAPI()

args = Arguments.init()

@app.get("/")
async def Home():
    """ Home route, mostly for testing """

    if args.hide_message:
        return {"message": "Disabled shutdown message"}
    else:
        return {"message": args.message}

@app.get("/shutdown")
async def GetShutdown():
    """ Shutdown route """

    Shutdown(args.message, args.hide_message, args.time)
    return {"message": args.message}

def main() -> None:
    """ Initialize the system tray icon and start the server """
    
    server_thread = threading.Thread(target=Server, args=(app, args))
    server_thread.start()

    with open("server.log", "w") as logFile:
        logFile.write("")

    Tray.Init()

if __name__ == "__main__":
    main()