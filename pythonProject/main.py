import time
import os

import requests
from bs4 import BeautifulSoup
import helpers

FREQUENCY = 5 * 60
PATH_TO_LINKS = "websites.txt"


def get_page_content(_url):
    get_site = requests.get(_url)
    if get_site.status_code >= 500:
        return "Server Error"
    elif get_site.status_code >= 400:
        return "Request Error"
    elif get_site.status_code >= 300:
        return "Relocated"
    elif get_site.status_code >= 200:
        return get_site.content
    else:
        return "UnKnown"


def content_has_changed(filename, content):
    page_body = BeautifulSoup(content, 'html.parser').find('body')
    content = page_body.text.replace("\n\n", "")

    try:
        with open(filename, 'r') as file:
            old_content = ""
            for line in file:
                old_content += line
            write_content(filename, content)
            if old_content == content:
                return False
            else:
                print("Changes\n" + helpers.find_changed_parts(old_content, content)[:200])
                return True

    except FileNotFoundError:
        write_content(filename, str(page_body.prettify()))
        return False


def send_email(message):
    pass


def write_content(filename, _new_content):
    with open(filename, 'w') as file:
        file.write(_new_content)
        with open(".gitignore", "a") as f:
            file.write(filename)


def get_websites(path):
    try:
        with open(path, 'r') as file:
            return [line for line in file]
    except FileNotFoundError:
        return []


while True:
    changed_sites = []
    for url in get_websites(PATH_TO_LINKS):
        incoming_content = get_page_content(url.replace("\n", ""))
        names = helpers.get_names_from_url(url)[0]
        name = ""
        if len(names) > 1:
            
        else:
            name = names[0]

        if len(incoming_content) > 100 and content_has_changed(f"{name}.txt", incoming_content):
            changed_sites.append([name, url])
            print(name + "***    content has changed\n")
        else:
            print(name + "     Nothing changed\n")

    send_email(changed_sites)
    time.sleep(FREQUENCY)
