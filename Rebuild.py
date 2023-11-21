import tkinter
import tkinter.messagebox
import customtkinter
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QCheckBox, QLineEdit, QPushButton, QLabel, QTextEdit
from PyQt5.QtGui import QIcon

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
# configure window
        self.title("Ad Assist Pro 2.0")
        self.geometry(f"{1100}x{580}")

# configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

if __name__ == "__main__":
    app = App()
    app.mainloop()