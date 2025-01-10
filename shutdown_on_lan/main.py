from fastapi import FastAPI
import uvicorn
import os
import argparse
import pystray
from PIL import Image, ImageDraw
import threading

app = FastAPI()

# Define the argument parser globally
parser = argparse.ArgumentParser(description="Shutdown On Lan")
parser.add_argument("--port", type=int, default=8000, help="Port to run the FastAPI app on (default: 8000)")
parser.add_argument("--message", type=str, default="The system will shut down in 5 seconds", help="Shutdown message (default: The system will shut down in 5 seconds)")
parser.add_argument("--hide-message", action='store_true', help="Hide shutdown message if specified")
args = parser.parse_args()

@app.get("/")
async def Home():
    if args.hide_message:
        return {"message": "Disabled shutdown message"}
    else:
        return {"message": args.message}

@app.get("/shutdown")
async def GetShutdown():
    Shutdown(args.message, args.hide_message)
    return {"message": args.message}

def Shutdown(message, hide_message):
    if hide_message:
        os.system("shutdown /s /t 5")
    else:
        os.system(f"shutdown /s /t 5 /c \"{message}\"")

def create_image():
    # Generate an image for the system tray icon
    width = 64
    height = 64
    image = Image.new('RGB', (width, height), (255, 255, 255))
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2 - 10, height // 2 - 10, width // 2 + 10, height // 2 + 10),
        fill=(0, 0, 0))
    return image

def on_quit(icon, item):
    icon.stop()
    os._exit(0)

def main():
    # Run the FastAPI app in a separate thread
    threading.Thread(target=lambda: uvicorn.run(app, host="0.0.0.0", port=args.port)).start()

    # Create the system tray icon
    icon = pystray.Icon("shutdown-on-lan")
    icon.icon = create_image()
    icon.menu = pystray.Menu(pystray.MenuItem("Quit", on_quit))
    icon.run()

if __name__ == "__main__":
    main()