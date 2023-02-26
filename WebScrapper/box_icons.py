import requests
from bs4 import BeautifulSoup

item_class = "Filter_filter_bottom__P2_wa"
get_site = requests.get("https://boxicons.com/")
print(get_site.status_code)
page = BeautifulSoup(get_site.content, "lxml")
div = page.find(class_=item_class)
for item in div:
    print(
        item
    )
