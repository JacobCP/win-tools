import tkinter
from tkinter import filedialog


def get_windows_directory():
    tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
    folder_path = filedialog.askdirectory()

    return folder_path
