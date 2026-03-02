from pathlib import Path
 
dirs = {".jpg": "Images",
        ".png": "Images",
        ".bmp": "Images",
        ".gif": "Videos",
        ".mp4": "Videos",
        ".avi": "Videos",
        ".txt": "Documents",
        ".pptx": "Documents",
        ".csv": "Documents",
        ".xls": "Documents",
        ".odp": "Documents",
        ".pdf": "Documents",
        ".mp3": "Musiques",
        ".wav": "Musiques",
        ".flac": "Musiques"}
 
tri_dir = Path(r"C:\Users\Toto\Downloads")
files = [f for f in tri_dir.iterdir() if f.is_file()]
for f in files:
    # Si aucune correspondance n'est trouvé pour l'extension, on place les fichiers dans un dossier Divers
    output_dir = tri_dir / dirs.get(f.suffix, "Divers")
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)