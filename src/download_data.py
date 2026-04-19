import os
import zipfile
import urllib.request

print("Downloading dataset...")

# Create data folder
os.makedirs("data", exist_ok=True)

# Correct dataset ZIP URL
url = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
zip_path = "data/ml-latest-small.zip"

# Download zip
urllib.request.urlretrieve(url, zip_path)

print("Download complete. Extracting...")

# Extract zip
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall("data")

print("Extraction done!")

# Move required files
import shutil

shutil.move("data/ml-latest-small/movies.csv", "data/movies.csv")
shutil.move("data/ml-latest-small/ratings.csv", "data/ratings.csv")

print("✅ Dataset ready inside data folder")