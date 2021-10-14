import os
from PyPDF2 import PdfFileMerger

from tool_helpers import win_explorer


def merge_pdf_files(dir_path):
    pdfs = [file_name for file_name in os.listdir(dir_path) if file_name[-4:] == ".pdf"]

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(os.path.join(dir_path, pdf))

    merger.write(os.path.join(dir_path, "all_pdfs.pdf"))
    merger.close()


if __name__ == "__main__":
    pdf_dir_path = win_explorer.get_windows_directory()
    merge_pdf_files(pdf_dir_path)
