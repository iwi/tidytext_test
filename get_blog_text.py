#!/python3

from bs4 import BeautifulSoup
import requests
import csv
import sys
import json
import pickle

# Start by installing PyMedium and running it on a flask
# https://github.com/enginebai/PyMedium

# go back and repeat

def get_medium_posts_from(username):
    page = requests.get('http://localhost:5000/@{}/posts'.format(username))
    soup = str(BeautifulSoup(page.content, 'html.parser'))
    posts_data = json.loads(soup)
    urls = list(map((lambda x: x['url']), posts_data))
    return(urls)

def get_text_only(url):
    page = requests.get(url)
    parsed = BeautifulSoup(page.content, 'html.parser')
    all_p = parsed.find_all('p')
    text_list = list(map(BeautifulSoup.get_text, all_p))
    text = ''.join(text_list)
    return(text)


if __name__ == '__main__':
    # Get the ame of the user 
    weeknotes_writer = input("Please type the medium username of the weeknotes writer:\n")

    # Get the latest urls from the writer and add them to the old ones
    latest_urls = get_medium_posts_from(weeknotes_writer)
    try:
        with open ("old_url_weeknotes_{}.pkl".format(weeknotes_writer), 'rb') as fp:
            old_urls = list(pickle.load(fp))
    except:
        old_urls = []

    urls = latest_urls + old_urls
    urls = set(urls)  # ignore duplicates

    # Save the imported urls for future use
    with open("old_url_weeknotes_{}.pkl".format(weeknotes_writer), 'wb') as fp:
            pickle.dump(urls, fp)

    # Get the text from the urls
    texts = []
    for url in urls:
        text = get_text_only(url)
        texts.append(text)

    # Save the text of the weeknotes 
    with open("weeknotes_{}.csv".format(weeknotes_writer), "w", newline = "") as fout:
        writer = csv.writer(fout, delimiter = ',')
        writer.writerow(urls)
        writer.writerow(texts)

        # writer = csv.DictWriter(fout,
        #                     fieldnames = urls,
        #                     delimiter = ',')
        # writer.writerow(texts)
