import os
from typing import List

l: List[str] = []

def dir_loop():
    for root, dirs, files in os.walk("F:\Файлы\PDF_notes\lib"):
        for file in files:
            if file.endswith(".pdf"):
                l.append([(os.path.join(file)), root])
    return l
