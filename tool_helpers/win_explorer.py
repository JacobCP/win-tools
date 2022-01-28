import tkinter
from tkinter import filedialog, simpledialog
from tkcalendar import Calendar, DateEntry


def get_windows_directory():
    tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
    folder_path = filedialog.askdirectory()

    return folder_path


def get_windows_file():
    tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
    file_path = filedialog.askopenfilename()

    return file_path


def get_string(title, prompt):
    tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
    user_string = simpledialog.askstring(title, prompt)

    return user_string
