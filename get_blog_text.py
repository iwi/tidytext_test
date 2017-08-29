#!/python3

from bs4 import BeautifulSoup
import requests
import csv
import sys


def get_text_only(url):
    page = requests.get(url)
    parsed = BeautifulSoup(page.content, 'html.parser')
    all_p = parsed.find_all('p')
    text_list = list(map(BeautifulSoup.get_text, all_p))
    text = ''.join(text_list)
    return(text)


if __name__ == '__main__':
    # Urls to get
    urls = [
        'https://medium.com/@drryandunn/weeknotes-s02-e01-68af74d9e96b',
        'https://medium.com/@drryandunn/weeknotes-s01e09-7135e6d4c4d7',
        'https://medium.com/@drryandunn/weeknotes-s01e08-c50fef5ace1a',
        'https://medium.com/@drryandunn/weeknotes-s01e07-378ef801057d',
        'https://medium.com/@drryandunn/weeknotes-s01e06-1f119808daa4',
        'https://medium.com/@drryandunn/weeknotes-s01e05-6d0020c9b335',
        'https://productforthepeople.xyz/weeknotes-s01e04-6a21a20ac6b0',
        'https://productforthepeople.xyz/weeknotes-s01e03-2caaa58a0547',
        'https://productforthepeople.xyz/weeknotes-s01e02-674e81f44797',
        'https://productforthepeople.xyz/weeknotes-s01-e01-af39311da6c4'
    ]

    texts = []

    for url in urls:
        text = get_text_only(url)
        texts.append(text)

    with open("weeknotes_ryan.csv", "w", newline="") as fout:
        writer = csv.writer(fout, delimiter=',')
        writer.writerow(texts)
