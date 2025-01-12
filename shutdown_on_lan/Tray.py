import os
import pystray
import threading
import time
from PIL import Image, ImageTk
import customtkinter as tk
from shutdown_on_lan.CreateImage import CreateImage
from shutdown_on_lan.CtkScrollableTextDisabled import CtkScrollableTextDisabled

def Init() -> None:
    """ Create the system tray icon """

    tray = pystray.Icon("shutdown-on-lan")

    try:
        tray.icon = Image.open("assets/python.png")
    except FileNotFoundError:
        tray.icon = CreateImage()
    tray.menu = pystray.Menu(
        pystray.MenuItem("Show Logs", ShowLogs),
        pystray.MenuItem("Quit", OnQuit)
    )

    tray.run()

def OnQuit(tray) -> None:
    """ Button to close the program from the system tray icon """

    tray.stop()
    os._exit(0)

def ShowLogs() -> None:
    """ Show the logs in a window """

    logViewerRoot = tk.CTk()
    
    logViewerRoot.geometry("600x400")
    logViewerRoot.title("shutdown-on-lan: Log Viewer")

    textArea = CtkScrollableTextDisabled(logViewerRoot, width=100, height=30)
    textArea.pack(expand=True, fill='both')

    logThread = threading.Thread(target=TailLogs, daemon=True, args=(textArea,))
    logThread.start()

    logViewerRoot.protocol("WM_DELETE_WINDOW", lambda: OnClosing(logViewerRoot, logThread))
    logViewerRoot.mainloop()

def TailLogs(textArea: CtkScrollableTextDisabled) -> None:
    """ Continuously read the log file and update the text in the window """

    global stopTail
    stopTail = False

    with open("server.log", "r") as logFile:
        while True:
            if stopTail:
                break

            logLine = logFile.readline()

            if logLine:
                textArea.insert(logLine)
            else:
                time.sleep(0.1)


def OnClosing(logViewerRoot: tk.CTk, logThread: threading.Thread) -> None:
    """ Close the log viewer window """

    global stopTail
    stopTail = True

    logThread.join()
    
    logViewerRoot.destroy()