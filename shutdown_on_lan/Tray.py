import os
import pystray
from shutdown_on_lan.CreateImage import CreateImage

def Init() -> None:
    """ Create the system tray icon """
    icon = pystray.Icon("shutdown-on-lan")
    icon.icon = CreateImage()
    icon.menu = pystray.Menu(
        # pystray.MenuItem("Show Logs", show_logs),
        pystray.MenuItem("Quit", on_quit)
    )
    icon.run()

def on_quit(icon) -> None:
    icon.stop()
    os._exit(0)