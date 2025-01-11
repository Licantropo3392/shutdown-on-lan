import os
import pystray
import threading
import time
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from shutdown_on_lan.CreateImage import CreateImage

def Init() -> None:
    """ Create the system tray icon """
    tray = pystray.Icon("shutdown-on-lan")
    tray.icon = CreateImage()
    tray.menu = pystray.Menu(
        pystray.MenuItem("Show Logs", ShowLogs),
        pystray.MenuItem("Quit", OnQuit)
    )
    tray.run()

def OnQuit(tray) -> None:
    tray.stop()
    os._exit(0)

def ShowLogs() -> None:
    logViewerRoot = tk.Tk()
    logViewerRoot.title("Log Viewer")

    textArea = ScrolledText(logViewerRoot, wrap=tk.WORD, width=100, height=30)
    textArea.pack(expand=True, fill='both')

    logThread = threading.Thread(target=TailLogs, daemon=True, args=(textArea,))
    logThread.start()

    logViewerRoot.mainloop()

def TailLogs(textArea: ScrolledText) -> None:
    with open("server.log", "r") as logFile:
        while True:
            logLine = logFile.readline()
            if logLine:
                textArea.configure(state=tk.NORMAL)
                textArea.insert(tk.END, logLine)
                textArea.see(tk.END)
                textArea.configure(state=tk.DISABLED)
            else:
                time.sleep(0.1)