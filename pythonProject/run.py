import os
import requests
import selenium 
from bs4 import BeautifulSoup
from urllib.request import urlopen
from helpers import get_websites, directory_name, create_directory, add_to_gitignore

from  constants import PATH_TO_LINKS as websites

def check_url_connection(url):  
    try:
        response = requests.get(url)     
        if response.status_code == requests.codes.ok:
            print('successful')
        else:
            response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"{e}")



def extract_website_data(url):
    page = urlopen(url)
    html = page.read().decode('utf-8')
    content = BeautifulSoup(html,'html.parser')
    
    
    return content.prettify()
    

   

def store_extract_data_in_file(url):
    #store data in the specified directory
    print(url)
    directory = directory_name(url)
    
    if directory is None:
        create_directory(directory)
        add_to_gitignore(directory)
        cwd = os.getcwd()
        os.chdir(directory)

        with open('new_index.html','w') as index:
            index.write(extract_website_data(url))

        print('Content has been successfully stored')
        os.chdir(cwd)
     
    
def detect_changes(prev_data, current_data):
    pass


def send_notification(changes):
    pass

def main():

    
    # Loop through each website and monitor changes
    for website in get_websites(websites):
        check_url_connection(website)
        store_extract_data_in_file(website)

        
        














main()