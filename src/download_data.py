from pathlib import Path
import kagglehub
import shutil

DATASET = "varunchawla30/german-credit-data"
RAW_DIR = Path("data/raw")

RAW_DIR.mkdir(parents=True, exist_ok=True)

# Download dataset to kagglehub cache
path = kagglehub.dataset_download(DATASET)
print("Downloaded to cache:", path)

# Copy files into data/raw
src_path = Path(path)
for file in src_path.rglob("*"):
    if file.is_file():
        shutil.copy2(file, RAW_DIR / file.name)

print("Files copied to:", RAW_DIR.resolve())