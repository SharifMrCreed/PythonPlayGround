from colorama import Fore


def get_color(status_code):
    color = Fore.GREEN
    if status_code >= 500:
        color = Fore.CYAN
    elif status_code >= 400:
        color = Fore.RED
    elif status_code >= 300:
        color = Fore.BLUE
    elif status_code >= 200:
        color = Fore.GREEN
    elif status_code >= 100:
        color = Fore.LIGHTMAGENTA_EX
    return color


def write_strings_to_csv_file(file_name, strings_list, mode='a'):
    """
    This function tactically helps to write to a csv file. Its usage should be intuitive though.
    :param file_name: the name of the csv file to write to
    :param mode: the mode of writing either 'w' or 'a'
    :param strings_list: the list of strings to be written to the csv file. they must correspond to a single row entry
    """
    if mode is not ('w' or 'a'):
        mode = 'a'

    not_allowed = ["", "\n"]
    clean_list = []
    for item in strings_list:
        if not not_allowed.__contains__(item):
            clean_list.append(item)

    with open(file_name, mode) as file:
        for item in clean_list:
            if item == clean_list[-1]:
                file.write(item)
            else:
                file.write(item + ",")

        file.write("\n")


def print_csv_file(file_name):
    """
    Prints the contents of a csv file to the console in a non beautified way
    :param file_name: name of the file to print
    """
    with open(file_name, 'r') as file:
        for line in file:
            print(line)
