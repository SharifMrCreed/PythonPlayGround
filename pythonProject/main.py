import time
import os

import requests
from bs4 import BeautifulSoup
import helpers


FREQUENCY = 5 * 60
PATH_TO_LINKS = "websites.txt"
project = os.getcwd()



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
        return "UnKnown Error"


def content_has_changed(filename, content):
    page_body = BeautifulSoup(content, 'html.parser').find('body')
    content = page_body.text.replace("\n\n", "")

    try:
        with open(filename, 'r', encoding="utf-8") as file:
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
    if filename == "":
        return
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(_new_content)



while True:
    changed_sites = []
    directories = []
    for url in helpers.get_websites(PATH_TO_LINKS):
        incoming_content = get_page_content(url.replace("\n", ""))
        parts = helpers.get_names_from_url(url)
        directories = parts[0]
        files = parts[1]
        name = ""
        directory = ""

        helpers.add_to_gitignore(directories[0]+"\n")

        for n in directories:
            directory = helpers.create_directory(n)
            os.chdir(directory)

        if len(files) == 1 and files[0] == '':
            name = directories[0]
        else:
            for x in files:
                name += f"_{x}"

        if len(incoming_content) > 100 and content_has_changed(f"{name}.txt", incoming_content):
            changed_sites.append([name, url])
            print(name + "***    content has changed\n")
        else:
            print(name + "     Nothing changed\n")
        os.chdir(project)

    send_email(changed_sites)
    time.sleep(FREQUENCY)
