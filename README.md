# Analysis of Wikipedia Article Length Across Languages

Read the full article here: https://www.julienverneaut.com/en/articles/which-country-has-most-content-wikipedia

## Objective

This project explores whether English Wikipedia articles tend to be longer and richer in content compared to their French counterparts.

## Methodology

To investigate, I analyzed the length of Wikipedia articles in various languages. I used the Wikipedia API to collect data. Due to API limitations (50 random articles content at a time), I first calculated the average bytes per character using this API, then used another more permissive API to fetch article lengths (500 articles at a time). This approach enabled me to determine the number of characters for a large set of articles.

### Key Findings

On average, English Wikipedia articles contain 19% more information than French articles.

## Getting the Dataset

1. **Download 100 000 articles and their lengths without content for each studied language:**
   ```bash
   python3 scripts/fetch_random_articles.py
   ```

2. **Download 500 articles with content and their lengths for each studied language:**
   ```bash
   python3 scripts/fetch_random_articles_content.py
   ```

## Processing the Data

> Pre-processed data is available in the `data/processed` folder.

1. **Process the dataset to get the average byte sizes of articles for each language:**
   ```bash
   python3 scripts/process_articles_byte_size.py
   ```

2. **Process the dataset to get the average bytes per character for each language:**
   ```bash
   python3 scripts/process_articles_bytes_per_char.py
   ```

These commands will generate two files:
- `data/processed/articles_byte_size.csv`: Contains statistics (average, standard deviation, mean, 1st, and 3rd quartiles) of article byte sizes for each language.
- `data/processed/articles_bytes_per_char.csv`: Contains statistics of bytes per character for each language.

## Analysis

For detailed results, see `notebooks/analyis.ipynb`.
