ARTICLES_ITERATIONS=200

import requests
import json
import os

languages = ["en", "ceb", "sv", "de", "fr", "nl", "ru", "es", "it", "pl", "war", "vi", "ja", "zh", "pt"]

def getRandomArticlesUrl(locale):
    return "https://" + locale + ".wikipedia.org/w/api.php?action=query&generator=random&grnlimit=500&grnnamespace=0&prop=info&format=json"

def getRandomArticles(locale):
    url = getRandomArticlesUrl(locale)
    response = requests.get(url)
    return json.loads(response.content)["query"]["pages"]

for i in range(len(languages)):
    language = languages[i]

    directory = f"data/raw/random_articles/{language}"
    os.makedirs(directory, exist_ok=True)

    print('-' * 80)
    print(f"{i + 1}/{len(languages)} Fetching articles for {language}...")

    for j in range(ARTICLES_ITERATIONS):
        print(f"   {j + 1}/{ARTICLES_ITERATIONS} Fetching articles for {language} iteration {j}...")
        random_articles = getRandomArticles(language)
        filename = f"articles-{language}-{j}.json"

        with open(f"{directory}/{filename}", "w") as f:
            f.write(json.dumps(random_articles))

    print(f"Fetching articles for {language} done!")

print("\nDone fetching articles!")
