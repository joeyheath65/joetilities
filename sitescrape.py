import requests
from bs4 import BeautifulSoup
import csv

print("Joe's CSV Diff Utility!"
      "***   USAGE NOTE   ***"
      "This utility will compare the first column of 2 .csv files and print out"
      "which lines are not present in CSV2 that ARE present in CSV1 and vice versa.")

# URL of the webpage to scrape
url = 'https://search.arin.net/rdap/?query=HEB*'  # Replace with the URL you want to scrape

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the data you want from the HTML (example: extracting all <a> tags)
    links = soup.find_all('a')

    # Create a list to hold the data
    data = []

    for link in links:
        # Extract the text and href attribute of each <a> tag
        link_text = link.get_text()
        link_href = link['href']

        # Add the data to the list
        data.append([link_text, link_href])

    # Define the CSV file name
    csv_file_name = 'webpage_data.csv'

    # Write the data to a CSV file
    with open(csv_file_name, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write the header row (optional)
        csv_writer.writerow(['Link Text', 'Link Href'])
        # Write the data rows
        csv_writer.writerows(data)

    print(f'Data has been scraped and saved to {csv_file_name}')
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
