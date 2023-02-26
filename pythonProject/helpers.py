import urllib.parse
import os


def get_names_from_url(url):
    if not string_is_url(url):
        raise ValueError(f"{url} is not a url btw")

    # Split the url using the / as the delimiter
    dirty_parts = url.split("/")
    not_allowed = ["http:", "https:", "www", ""]

    # looking for the actual domain to get the name of the website. I think what ever comes
    # Before the .com is the Name of the site.
    directories = []
    clean_parts = []
    for part in dirty_parts:
        if not_allowed.__contains__(part.lower()):
            continue
        if part.__contains__("."):
            if len(directories) > 0:
                clean_parts.append(''.join(c for c in part if c.isalnum())[:15])
                continue
            other_parts = part.split(".")
            if len(other_parts) > 0:
                for other_part in other_parts:
                    if not_allowed.__contains__(other_part.lower()):
                        continue
                    if other_part.lower() == "com":
                        break
                    else:
                        directories.insert(0, ''.join(c for c in other_part if c.isalnum())[:15])
        else:
            clean_parts.append(''.join(c for c in part if c.isalnum())[:15])

    return [directories, clean_parts]


def string_is_url(string):
    if not string.__contains__("http") or string.__contains__(" ") or string.__contains__("<") or string.__contains__(
            ">") or string.__contains__("{") or string.__contains__("}"):
        return False
    try:
        result = urllib.parse.urlparse(string)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def find_changed_parts(string1, string2):
    changed_parts = ""
    if len(string1) > len(string2):
        shorter_string = string2
    else:
        shorter_string = string1

    for i in range(len(shorter_string)):
        if string1[i] != string2[i]:
            changed_parts += string2[i]

    if len(string2) > len(shorter_string):
        changed_parts += string2[len(shorter_string):]
    return changed_parts


def create_directory(name):
    directory = os.getcwd()
    path = os.path.join(directory, name)
    try:
        os.mkdir(path)
    except FileExistsError:
        pass
    return path


def add_to_gitignore(filename):
    with open(".gitignore", "r") as file:
        ignored = [line for line in file]
        if not ignored.__contains__(filename):
            with open(".gitignore", "a") as f:
                f.write(filename)



