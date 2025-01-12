import os

def Shutdown(message, hide_message, time) -> None:
    """ Shutdown the system with a message if specified """

    if hide_message:
        os.system(f"shutdown /s /t {time}")
    else:
        os.system(f"shutdown /s /t {time} /c \"{message}\"")