import os
import json
import statistics
import numpy as np

languages = ["en", "ceb", "sv", "de", "fr", "nl", "ru", "es", "it", "pl", "war", "vi", "ja", "zh", "pt"]

def process_articles_bytes_per_char(folder):
    sizes = []

    for filename in os.listdir(folder):
        with open(f"{folder}/{filename}", "r") as f:
            data = json.load(f)
            for key in data:
                byte_size = data[key]["revisions"][0]["size"]
                char_count = len(data[key]["revisions"][0]["*"])

                sizes.append(byte_size / char_count)

    average = statistics.mean(sizes)
    stdev = statistics.stdev(sizes)
    quantiles = np.percentile(sizes, [25, 50, 75])

    return average, stdev, quantiles

os.makedirs("data/processed", exist_ok=True)

with open("data/processed/articles_bytes_per_char.csv", "w") as f:
    f.write("language,average,stdev,25th percentile,50th percentile,75th percentile\n")

for language in languages:
    directory = f"data/raw/random_articles_content/{language}"
    average, stdev, quantiles = process_articles_bytes_per_char(directory)

    with open("data/processed/articles_bytes_per_char.csv", "a") as f:
        f.write(f"{language},{average},{stdev},{quantiles[0]},{quantiles[1]},{quantiles[2]}\n")
