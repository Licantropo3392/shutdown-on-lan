from customtkinter import CTkScrollableFrame, CTkLabel
import tkinter as tk

class CtkScrollableTextDisabled():
    def __init__(self, root, width, height):
        self.root = root
        self.width = width
        self.height = height

        self.frame = CTkScrollableFrame(self.root)

        self.textArea = CTkLabel(self.frame, text="", width=self.width, height=self.height)

    def pack(self, expand, fill):
        self.frame.pack(expand=expand, fill=fill)
        self.textArea.pack(expand=expand, fill=fill)

    def insert(self, text):
        self.textArea.configure(state=tk.NORMAL)
        self.textArea.configure(text=self.textArea.cget("text") + text)
        self.textArea.configure(state=tk.DISABLED)

        self.frame._parent_canvas.yview_moveto(1.0)

    def destroy(self):
        self.frame.destroy()