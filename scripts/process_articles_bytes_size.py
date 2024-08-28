import os
import json
import statistics
import numpy as np

languages = ["en", "ceb", "sv", "de", "fr", "nl", "ru", "es", "it", "pl", "war", "vi", "ja", "zh", "pt"]

def process_articles_byte_size(folder):
    sizes = []

    for filename in os.listdir(folder):
        with open(f"{folder}/{filename}", "r") as f:
            data = json.load(f)
            for key in data:
                sizes.append(data[key]["length"])

    average = statistics.mean(sizes)
    stdev = statistics.stdev(sizes)
    quantiles = np.percentile(sizes, [25, 50, 75])

    return average, stdev, quantiles

os.makedirs("data/processed", exist_ok=True)

with open("data/processed/articles_byte_size.csv", "w") as f:
    f.write("language,average,stdev,25th percentile,50th percentile,75th percentile\n")

for language in languages:
    directory = f"data/raw/random_articles/{language}"
    average, stdev, quantiles = process_articles_byte_size(directory)

    with open("data/processed/articles_byte_size.csv", "a") as f:
        f.write(f"{language},{average},{stdev},{quantiles[0]},{quantiles[1]},{quantiles[2]}\n")
