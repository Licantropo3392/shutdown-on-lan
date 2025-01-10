import os

def Shutdown(message, hide_message) -> None:
    """ Shutdown the system with a message if specified """
    if hide_message:
        os.system("shutdown /s /t 5")
    else:
        os.system(f"shutdown /s /t 5 /c \"{message}\"")