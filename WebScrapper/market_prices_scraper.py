# This is a sample web scrapper. We shall be scrapping
# the website http://www.agromarketday.com/markets/12-owino-market
# to see how the data changes daily
import datetime
from pprint import pprint

from bs4 import BeautifulSoup
import requests
import colorama
from helpers import (
    get_color,
    write_strings_to_csv_file,
    print_csv_file
)

# Program start

colorama.init(autoreset=True)

url = "http://www.agromarketday.com/markets/12-owino-market"
get_site = requests.get(url)

# Let's check the response
print(get_color(get_site.status_code), get_site.headers)

page = BeautifulSoup(get_site.content, "lxml")
prices_table = page.find(class_="table table-striped table-market-prices")

table_head = prices_table.thead
date = str(datetime.date.today())
file_name = f"marketPricesOn{date}.csv"
write_strings_to_csv_file(file_name=file_name, strings_list=[tag.string for tag in table_head.children],
                          mode='w')

table_rows = prices_table.findAll('tr')
strings_lists = []
for row in table_rows:
    write_strings_to_csv_file(file_name=file_name, strings_list=[tag.string for tag in row.children])

# print(table_rows)
print_csv_file(file_name=file_name)
