import pdfplumber

from gtts import gTTS
from os.path import join, abspath
from pathlib import Path


FILE_NAME = "antalya_facts.pdf"
FOLDER_PATH = "."
file_path = join(FOLDER_PATH, FILE_NAME)
file_path = Path(abspath(file_path))


def check_exist(file_path):
    """Checks if the file exists and it's a '.pdf' file."""
    if file_path.is_file() and file_path.suffix == ".pdf":
        return True
    return False
        

def convert_to_mp3(path, lang="en"):
    """Converts pdf file to mp3 with gtts."""
    if check_exist(path):
        print("Converting...")
        with pdfplumber.PDF(open(file=path, mode="rb")) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = "".join(pages)
        text = text.replace("\n", "")
        mp3 = gTTS(text=text, lang=lang)
        file_name = path.stem
        file_name += ".mp3"
        mp3.save(file_name)
        return "Completed!"
    return "Something's wrong!"

print(convert_to_mp3(file_path))
