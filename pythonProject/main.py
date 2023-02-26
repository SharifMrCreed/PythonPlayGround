import requests
from bs4 import BeautifulSoup


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
                print("Changes\n" + find_changed_parts(old_content, content)[:200])
                return True

    except FileNotFoundError:
        write_content(filename, str(page_body.prettify()))
        return False


def find_changed_parts(string1, string2):
    changed_parts = ""
    if len(string1) > len(string2):
        reference_string = string1
        shorter_string = string2
    else:
        reference_string = string2
        shorter_string = string1
    for i in range(len(shorter_string)):
        if shorter_string[i] != reference_string[i]:
            changed_parts += reference_string[i]
    if len(reference_string) > len(shorter_string):
        changed_parts += reference_string[len(shorter_string):]
    return changed_parts


def send_email(message):
    pass


def write_content(filename, _new_content):
    with open(filename, 'w') as file:
        file.write(_new_content)


def get_websites():
    _websites = []
    try:
        with open("websites.txt", 'r') as file:
            for line in file:
                _websites.append(line.split(","))
            return _websites

    except FileNotFoundError:
        return []


changed_sites = []
print(get_websites())
for name, url in get_websites():
    incoming_content = get_page_content(url.replace("\n", ""))

    if len(incoming_content) > 100 and content_has_changed(f"{name}.txt", incoming_content):
        changed_sites.append([name, url])
        print(name + "***    content has changed\n")
    else:
        print(name + "     Nothing changed\n")

send_email(changed_sites)
