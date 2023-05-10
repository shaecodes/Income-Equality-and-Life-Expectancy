import requests               # import the requests library to make HTTP requests
from bs4 import BeautifulSoup # import BeautifulSoup to parse HTML documents
import csv                    # import csv to read and write CSV files

url = "https://en.wikipedia.org/wiki/List_of_countries_by_income_equality"
response = requests.get(url)  # send a GET request to the URL and store the response

soup = BeautifulSoup(response.content, "html.parser") # parse the response using BeautifulSoup

# find the second table on the webpage
tables = soup.find_all("table")
second_table = tables[1]

headers = []
for th in second_table.find_all("th"):
    headers.append(th.text.strip())  # extract and add the headers to the headers list

rows = []
for tr in second_table.find_all("tr")[1:]:
    row = []
    for td in tr.find_all("td"):
        row.append(td.text.strip())  # extract and add each table cell value to the row list
    rows.append(row)  # add the row to the rows list

# write the extracted data to a CSV file
with open("income_equality.csv", mode='a', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)      # create a CSV writer object
    writer.writerow(headers)          # write the headers to the CSV file
    for row in rows:
        writer.writerow(row)          # write each row to the CSV file