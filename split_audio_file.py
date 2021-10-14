import os
from pydub import AudioSegment
import tkinter
from tkinter import filedialog


def split_audio_file(file_path, length_in_minutes=5):
    length_in_miliseconds = length_in_minutes * 1000 * 60

    directory_path, file_name, file_type = (
        os.path.dirname(file_path),
        os.path.basename(file_path)[:-4],
        os.path.basename(file_path)[-3:],
    )
    split_files_directory = os.path.join(directory_path, file_name)
    os.makedirs(split_files_directory)

    working_audio = AudioSegment.from_file(file_path, file_type)

    counter = 0
    while working_audio.duration_seconds > 0:
        new_audio = working_audio[:length_in_miliseconds]

        new_audio_file_name = f"{file_name}_{counter}.{file_type}"
        new_audio_file_path = os.path.join(split_files_directory, new_audio_file_name)
        new_audio.export(new_audio_file_path, format=file_type)
        working_audio = working_audio[length_in_miliseconds:]
        counter += 1


def split_audio_files_in_directory(directory_path, length_in_minutes=5):
    audio_file_names = os.listdir(directory_path)

    for audio_file_name in audio_file_names:
        audio_file_path = os.path.join(directory_path, audio_file_name)

        if os.path.isfile(audio_file_path):
            try:
                split_audio_file(audio_file_path, length_in_minutes=length_in_minutes)
                print(f"split {audio_file_name}")
            except Exception:
                print(f"failed to split {audio_file_name}")
                continue


def get_windows_directory():
    tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
    folder_path = filedialog.askdirectory()

    return folder_path


if __name__ == "__main__":
    audio_files_directory_path = get_windows_directory()
    split_audio_files_in_directory(audio_files_directory_path)
